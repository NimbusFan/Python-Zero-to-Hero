from pyspark import SparkConf, SparkContext

# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 以下这段等同于上面这一行（链式调用）的作用,
# conf = SparkConf()
# conf.setMaster("local[*]")
# conf.setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf = conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext对象的运行(停止PySpark程序)
sc.stop()