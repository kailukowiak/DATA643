import findspark
findspark.init()

from pyspark import SparkContext
sc = SparkContext("local", "First App")

sc.stop()
