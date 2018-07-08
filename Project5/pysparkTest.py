from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder

from pyspark.sql.types import FloatType
from pyspark.sql.functions import col

import pandas as pd

from pyspark import SparkContext, SparkConf

from pyspark.sql import SQLContext

sc = SparkContext
#sqlContext = SQLContext(sc)


# ratings = pd.read_csv('ml-latest-small/ratings.csv')

ratings = sc.textFile('ml-latest-small/ratings.csv')


# .toDF(["user",
#                                                            "item",
#                                                            "rating",
#                                                            "timestamp"])


X_train, X_test = ratings.randomSplit([0.6, 0.4])



