## Import libraries
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
from pyspark import SparkContext

import pandas as pd
from pyspark.sql import SQLContext

## Initialize Spark
sc = SparkContext('local', 'project5.1')
sql_sc = SQLContext(sc)

## Load data

pandas_df = pd.read_csv('Project2/ml-latest-small/ratings.csv')
# pandas_df = pandas_df.drop('timestamp', 1)
# pandas_df.columns = ['user', 'item', 'rating']
s_df = sql_sc.createDataFrame(pandas_df)

X_train, X_test = s_df.randomSplit([0.7, 0.3], seed=643)

## Training 
als = ALS(rank=10,
          maxIter=10,
          userCol='userId',
          itemCol='movieId',
          ratingCol='rating')
model = als.fit(X_train.select(['userId', 'movieId', 'rating']))
