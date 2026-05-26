from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'D:/Code/PycharmProject/python_learning/.venv/Scripts/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

#通过parallelize方法将Python对象加载到Spark内，成为RDD对象
rdd = sc.parallelize([1, 2, 3, 4, 5])

rdd2 = rdd.filter(lambda num : num % 2 == 0)
print(rdd2.collect())

sc.stop()