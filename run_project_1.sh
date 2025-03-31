#!/bin/bash

# Check if both arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <program_number 1-4> <number_of_fields>"
  exit 1
fi

PROGRAM_NUM=$1
NUM_FIELDS=$2

# Validate inputs
if ! [[ "$PROGRAM_NUM" =~ ^[1-4]$ ]]; then
  echo "Error: First argument must be a number between 1 and 4."
  exit 1
fi

if ! [[ "$NUM_FIELDS" =~ ^[1-9][0-9]*$ ]]; then
  echo "Error: Second argument must be a positive integer."
  exit 1
fi

# Step 1: Remove previous output
echo "Removing previous Hadoop output directory..."
hadoop fs -rm -r /user/johndavis/output_violation_counts

# Step 2: Run the Hadoop streaming job with 1 reducer
echo "Running Hadoop streaming job with mapper${PROGRAM_NUM}.py and reducer${PROGRAM_NUM}.py..."
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.name="Violation Count Job ${PROGRAM_NUM}" \
  -input /user/johndavis/input/Parking_Violations_Issued_-_Fiscal_Year_2017.csv \
  -output /user/johndavis/output_violation_counts \
  -mapper "./mapper${PROGRAM_NUM}.py" \
  -reducer "./reducer${PROGRAM_NUM}.py" \
  -file "mapper${PROGRAM_NUM}.py" \
  -file "reducer${PROGRAM_NUM}.py" \
  -numReduceTasks 1

# Step 3: Process the output
echo "Processing Hadoop output: Filtering lines with $NUM_FIELDS fields and sorting by field $NUM_FIELDS..."
hadoop fs -cat /user/johndavis/output_violation_counts/part-00000 | \
  awk -F'\t' "NF==$NUM_FIELDS" | \
  sort -t $'\t' -k${NUM_FIELDS},${NUM_FIELDS}nr | \
  head -n 25
