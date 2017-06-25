from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession\
            .builder\
            .appName("StructuredNetworkWordCount")\
            .config('spark.sql.warehouse.dir', 'file:///C:/temp/')\
            .getOrCreate()

# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = spark.readStream\
            .format("socket")\
            .option("host", "localhost")\
            .option("port", 9999)\
            .load()

# Split the lines into words
words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)

# Generate running word count
wordCounts = words.groupBy("word").count()

# Start running the query that prints the running counts to the console

query = wordCounts\
            .writeStream\
            .outputMode("complete")\
            .format("console")\
            .start()

# Mirar de evitar error al ejecutar query:
# pyspark.sql.utils.IllegalArgumentException: 'Pathname /C:/Users/Rubén/AppData/Local/Temp/temporary-f0d09ab6-7cac-4c54-aef0-87cab6d69678/offsets from C:/Users/Rubén/AppData/Local/Temp/temporary-f0d09ab6-7cac-4c54-aef0-87cab6d69678/offsets is not a valid DFS filename.'            
            
#.config("spark.sql.warehouse.dir", "file:///C:/temp/")\
#.config("spark.sql.warehouse.dir", "/C:/temp/")\
#.config("java.io.tmpdir", "/C:/temp/")\

#            .option("path", "file:///C:/temp/")\



#query.awaitTermination()


