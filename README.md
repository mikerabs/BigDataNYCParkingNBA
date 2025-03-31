# BigDataNYCParkingNBA
## 🚗 Hadoop Parking Violations Analysis

This project uses Hadoop Streaming to analyze parking violation data from the NYC Open Data set:  
**"Parking Violations Issued - Fiscal Year 2017"**

Python scripts (`mapper#.py`, `reducer#.py`) are used to define custom MapReduce jobs for different types of analyses. A bash script is provided to automate the process.

---

## 🛠 How to Use the Script

The script `run_hadoop_job.sh` automates the full process:

- Clears any existing output directory in HDFS.
- Runs a Hadoop Streaming job using the specified mapper and reducer pair.
- Processes the output by filtering, sorting, and displaying the top 25 results.

### 📄 Usage

```bash
bash run_hadoop_job.sh <program_number> <num_fields_in_output>
```

### 📌 Arguments

1. `program_number` (required)  
   - A number from **1 to 4** indicating which mapper and reducer to use.  
   - This corresponds to `mapper1.py`, `reducer1.py`, `mapper2.py`, etc.

2. `num_fields_in_output` (required)  
   - The number of **tab-separated fields** expected in the output.  
   - This is used to validate and sort the output properly.

### ✅ Example

```bash
bash run_hadoop_job.sh 2 3
```

This runs:
- `mapper2.py` and `reducer2.py`,
- Expects 3 tab-separated fields in the output,
- Sorts the output by the third field (numerically, descending),
- Displays the top 25 results.

---

## 🧠 How the Mappers and Reducers Work

This project uses the **Hadoop Streaming API**, which lets you write **mappers and reducers in Python** that read from `stdin` and write to `stdout`.

### 🔹 Mapper

Each `mapper#.py` script:
- Reads input lines (CSV rows from the parking violations dataset).
- Extracts relevant fields (e.g., violation type, issue date, plate state, etc.).
- Outputs **key-value pairs**, usually in the format:  
  ```
  Key<TAB>1
  ```
  Where `Key` is some field or combination of fields, and `1` represents a single occurrence.

### 🔹 Reducer

Each `reducer#.py` script:
- Reads sorted key-value pairs from the mapper.
- Aggregates counts by key.
- Outputs final key-count results:
  ```
  Key<TAB>Count
  ```
  Or, depending on the program, multiple fields like:
  ```
  Key1<TAB>Key2<TAB>Count
  ```

---

## 📁 Data Input Location

The input dataset must already be uploaded to HDFS at:

```
/user/johndavis/input/Parking_Violations_Issued_-_Fiscal_Year_2017.csv
```

If it’s not yet uploaded, you can do so using:

```bash
hadoop fs -mkdir -p /user/johndavis/input
hadoop fs -put Parking_Violations_Issued_-_Fiscal_Year_2017.csv /

