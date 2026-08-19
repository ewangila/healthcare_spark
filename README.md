# Healthcare Spark

A foundational **PySpark** project that demonstrates `SparkContext` setup, configuration, and basic distributed processing.

This repository serves as a starting point for exploring Apache Spark in a healthcare data context (or any other domain that needs scalable data processing).

## Features

- SparkContext initialization with custom configuration
- Exploration of key SparkContext attributes and settings
- Simple RDD creation and action (sum of a parallelized range)
- Log level configuration
- Ready for extension to real healthcare datasets (CSV, Parquet, etc.)

## Project Structure
```healthcare_spark/
├── spark_demo.py      # Main demo script
├── LICENCE            # MIT License
├── .gitignore
└── README.md
```
## Prerequisites

- Python 3.8+
- Java 8 or 11 (required by Spark)
- Apache Spark / PySpark

## Usage
Run the demo:
```Bash
python spark_demo.py
```
The script will:

1. Initialize findspark
2. Create a local SparkContext (local[*])
3. Print useful configuration and runtime information
4. Create a small RDD and compute its sum
5. Stop the SparkContext cleanly

   
