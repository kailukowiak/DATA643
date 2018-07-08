import findspark
findspark.init()

import pyspark
sc = pyspark.SparkContext(appName="myAppName")
