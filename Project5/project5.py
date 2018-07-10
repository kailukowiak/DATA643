## Import libraries
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
from pyspark import SparkContext
from pyspark.ml.linalg import 
from sklearn.metrics import mean_squared_error
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

## Predictions

preds = model.transform(X_test.select(['userId', 'movieId']))

## Validate

# I don't like the spark evaluator
preds = preds.toPandas()
## To pandas

val = pd.merge(pandas_df, preds, on=['userId', 'movieId'])
val = val.dropna() # Worryingly, we have na values. Possibly something to do
# With the train test split??
rmse = mean_squared_error(val.rating, val.prediction)
print(rmse)

# Thanks to:
# https://www.codementor.io/jadianes/building-a-recommender-with-apache-spark-python-example-app-part1-du1083qbw
# https://medium.com/@connectwithghosh/simple-matrix-factorization-example-on-the-movielens-dataset-using-pyspark-9b7e3f567536
# https://dataplatform.cloud.ibm.com/exchange/public/entry/view/99b857815e69353c04d95daefb3b91fa
