from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'D:\Code\PycharmProject\python_learning\.venv\Scripts\python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

#通过parallelize方法将Python对象加载到Spark内，成为RDD对象
rdd = sc.parallelize([('男', 99), ('男', 88), ('女', 99), ('女', 66)])

rdd2 = rdd.reduceByKey(lambda x, y: x + y)
print(rdd2.collect())