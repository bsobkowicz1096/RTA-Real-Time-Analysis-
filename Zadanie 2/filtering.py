from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, col

# Funkcja pomocnicza do wyświetlania danych strumieniowych
batch_counter = {"count": 0}
def process_batch(df, batch_id):
    batch_counter["count"] += 1
    print(f"Batch ID: {batch_id}")
    df.show(truncate=False)
    if batch_counter["count"] % 5 == 0:
        spark.stop()

# Utworzenie sesji Spark
spark = SparkSession.builder.appName("StreamingDemo").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Przygotowanie strumienia danych z format('rate')
rate_df = (spark.readStream
           .format("rate")
           .option("rowsPerSecond", 5)
           .load())

# Dodanie kolumn user_id i event_type
events = (rate_df
          .withColumn("user_id", expr("concat('u', cast(rand()*100 as int))"))
          .withColumn("event_type", expr("case when rand() > 0.7 then 'purchase' else 'view' end")))

# Wyfiltruj tylko 'purchase'
purchases = events.filter(col("event_type") == "purchase")

# Uruchomienie zapytania strumieniowego
query = (purchases.writeStream
         .format("console")
         .outputMode("append")
         .foreachBatch(process_batch)
         .start())

query.awaitTermination()