from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Funkcja pomocnicza do wyświetlania danych strumieniowych
batch_counter = {"count": 0}
def process_batch(df, batch_id):
    batch_counter["count"] += 1
    print(f"Batch ID: {batch_id}")
    df.show(truncate=False)
    if batch_counter["count"] % 5 == 0:
        spark.stop()

# Utworzenie sesji Spark
spark = SparkSession.builder.appName("RealTimeEcommerce").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Definicja schematu danych
schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("event_type", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("product_id", StringType(), True),
    StructField("category", StringType(), True),
    StructField("price", DoubleType(), True)
])

# Odczyt danych z katalogu
stream = (spark.readStream
          .schema(schema)
          .json("data/stream"))

# Sliding window - grupowanie typu zdarzeń w oknie o szerokości 5 minut, przesuwającym się co 1 minutę
windowed = (stream
            .withWatermark("timestamp", "1 minute")
            .groupBy(window("timestamp", "5 minutes", "1 minute"), "event_type")
            .count())

# Uruchomienie zapytania strumieniowego
query = (windowed
         .writeStream
         .outputMode("append")
         .foreachBatch(process_batch)
         .format("console")
         .start())

query.awaitTermination()