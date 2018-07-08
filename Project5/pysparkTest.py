from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder

from pyspark.sql.types import FloatType
from pyspark.sql.functions import col

import pandas as pd

from pyspark import SparkContext, SparkConf

from pyspark.sql import SQLContext



sc = SparkContext('local','project5')
sql_sc = SQLContext(sc)

pandas_df = pd.read_csv('Project2/ml-latest-small/ratings.csv')  

s_df = sql_sc.createDataFrame(pandas_df)



X_train, X_test = s_df.randomSplit([0.6, 0.4])


#sc.stop()
