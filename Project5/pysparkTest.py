## Load Libraries
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
# from pyspark.sql.types import FloatType
from pyspark.sql.functions import col
from pyspark import SparkContext
import pandas as pd
from pyspark.sql import SQLContext

## Initialize Spark
sc = SparkContext('local', 'project5')
sql_sc = SQLContext(sc)

## Load data
pandas_df = pd.read_csv('Project2/ml-latest-small/ratings.csv')  
pandas_df = pandas_df.drop('timestamp', 1)
pandas_df.columns = ['user', 'item', 'rating']
s_df = sql_sc.createDataFrame(pandas_df)

X_train, X_test = s_df.randomSplit([0.7, 0.3])

## Train 
als = ALS(rank=5, maxIter=10, seed=0)  # Change to same number as other example
model = als.fit(X_train.select(["user", "item", "rating"]))


## Test
predictions = model.transform(X_test.select(["user", "item"]))

## Validate

ratesAndPreds = X_test.join(predictions,(X_test.user == predictions.user)
                            & (X_test.item == predictions.item),
                            how='inner').select(X_test.user,X_test.item,
                                                X_test.rating,
                                                predictions.prediction)
# renaming the columns as raw and label
ratesAndPreds = ratesAndPreds.select([col("rating").alias("label"),
                                      col('prediction').alias("raw")])

ratesAndPreds = ratesAndPreds.withColumn("label",
                                         ratesAndPreds["label"].cast(FloatType()))
# calculate the error
evaluator = RegressionEvaluator(predictionCol="raw")
x = evaluator.evaluate(ratesAndPreds, {evaluator.metricName: "mae"})
