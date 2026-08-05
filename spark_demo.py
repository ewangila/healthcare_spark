import os
os.environ['JAVA_HOME'] = 'C:/Program Files/Eclipse Adoptium/jdk-11.0.31.11-hotspot'

import findspark
from pyspark import SparkConf, SparkContext
from py4j.protocol import Py4JError # Import the Py4JError exception class

# Initialize findspark to add PySpark to the system path
findspark.init()

# Create a SparkConf object
conf = SparkConf().setAppName("SparkContextDemo").setMaster("local[*]")

# Create a SparkContext
sc = SparkContext(conf=conf)
# Demonstrate various SparkContext attributes and settings

# Application Name
print("Application Name:", sc.appName)

# Master URL
print("Master URL:", sc.master)

# SparkConf
print("SparkConf:", sc.getConf().getAll())

# Default Parallelism
print("Default Parallelism:", sc.defaultParallelism)

# Default Minimum Partitions
print("Default Minimum Partitions:", sc.defaultMinPartitions)

# Spark Home
print("Spark Home:", sc.sparkHome)

# Spark User
print("Spark User:", sc.sparkUser())

# Spark Version
print("Spark Version:", sc.version)

# Python Version
print("Python Version:", sc.pythonVer)

statusTracker = sc.statusTracker()
active_jobs = statusTracker.getActiveJobsIds()
print("Active Job IDs:", active_jobs)

# List of Registered RDDs
print("Registered RDDs:", sc._jsc.getPersistentRDDs())

# Available Resources
print("Available Resources:", sc._jsc.sc().resources())

# Modify Log Level
sc.setLogLevel("WARN")

# Instead of using sc.getLogLevel(), you can access the log level from SparkConf:
log_level = sc.getConf().get("spark.logConf")
print("Current Log Level:", log_level)

# Alternatively, you can check the current log level using the following approach:
# import logging
# log_level = logging.getLogger("py4j").getEffectiveLevel()
# print("Current Log Level:", logging.getLevelName(log_level))

# Create a simple RDD and perform an action
rdd = sc.parallelize(range(10))
sum_result = rdd.sum()
print("Sum of RDD:", sum_result)

# Stop the SparkContext
sc.stop()
