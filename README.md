# Healthcare Spark

A foundational **PySpark** project that demonstrates `SparkContext` setup, configuration, and basic distributed processing.

This repository is a starting point for exploring Apache Spark, with a healthcare-oriented context in mind (easily adaptable to any domain that needs scalable data processing).

---

## Features

- SparkContext initialization with custom configuration
- Exploration of key SparkContext attributes and settings
- Simple RDD creation and action (sum of a parallelized range)
- Log level configuration
- Ready for extension to real healthcare datasets (CSV, Parquet, etc.)

---

## Project Structure

```text
healthcare_spark/
├── spark_demo.py      # Main demo script
├── LICENSE            # MIT License
├── .gitignore
└── README.md
```
## Prerequisites
* Python 3.8+
* Java 8 or 11 (required by Spark)
* Apache Spark / PySpark

## Installation
```
bash
pip install -r requirements.txt
```
## Usage
```
bash
python spark_demo.py
```
The script will:

1. Initialize `findspark`
2. Create a local SparkContext (`local[*]`)
3. Print useful configuration and runtime information
4. Create a small RDD and compute its sum
5. Stop the SparkContext cleanly

## Sample Output

```text
Application Name: SparkContextDemo
Master URL: local[*]
SparkConf: [...]
Default Parallelism: 8
Default Minimum Partitions: 2
Spark Home: ...
Spark User: ...
Spark Version: 3.x.x
Python Version: 3.x
Active Job IDs: []
Registered RDDs: {}
Available Resources: ...
Current Log Level: ...
Sum of RDD: 45
```
## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

**Author:** Eugin Wangila  
**Location:** Nairobi
