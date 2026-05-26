from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'D:\Code\PycharmProject\python_learning\.venv\Scripts\python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

#通过parallelize方法将Python对象加载到Spark内，成为RDD对象
rdd = sc.parallelize(["fan yun fei", "you qian duo jin", "niu bi 666"])

rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())