from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'D:/Code/PycharmProject/python_learning/.venv/Scripts/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

#通过parallelize方法将Python对象加载到Spark内，成为RDD对象
rdd = sc.parallelize([('itcast',4), ('python', 6),('itheima', 7),('spark',4),('pyspark', 3)])

rdd2 = rdd.sortBy(lambda x : x[1], ascending=False, numPartitions=1)
print(rdd2.collect())

sc.stop()