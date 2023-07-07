import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime


# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaCassandraIntegration") \
    .master("local[1]") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .config("spark.cassandra.auth.username", "cassandra") \
    .config("spark.cassandra.auth.password", "cassandra") \
    .config("spark.cassandra.connection.port", "9042") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")
# Configure Kafka consumer settings
kafka_bootstrap_servers = "kafka:9092"
kafka_topic = "hotel_data"
kafka_group_id = "test-consumer-group"

analyzer = SentimentIntensityAnalyzer()

def sentiment_analysis(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment["compound"]

sentiment_udf = udf(sentiment_analysis)



# Read data from Kafka topic as a DataFrame
df = spark.read.format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "earliest") \
    .load()
    # .option("group.id", kafka_group_id) \

# Convert the "value" column from binary to string
df = df.withColumn("value", col("value").cast("string"))
# Extract specific fields from the JSON string in the value field
format_df = df.select(
    expr("get_json_object(value, '$.hotel_url')").alias("hotel_url"),
    expr("get_json_object(value, '$.hotel_name')").alias("hotel_name"),
    expr("get_json_object(value, '$.total_hotel_reviews')").alias("total_hotel_reviews"),
    expr("get_json_object(value, '$.star')").cast("float").alias("star"),
    expr("get_json_object(value, '$.hotel_address')").alias("hotel_address"),
    expr("get_json_object(value, '$.price')").alias("price"),
    expr("get_json_object(value, '$.review_date')").alias("review_date"),
    expr("get_json_object(value, '$.reviewer_rating')").alias("reviewer_rating"),
    expr("get_json_object(value, '$.reviewer_contribution')").cast("integer").alias("reviewer_contribution"),
    expr("get_json_object(value, '$.reviewer_link')").alias("reviewer_link"),
    expr("get_json_object(value, '$.reviewer_title_comment')").alias("reviewer_title_comment"),
    expr("get_json_object(value, '$.reviewer_comment')").alias("reviewer_comment"),
    expr("get_json_object(value, '$.reviewer_stay_date')").alias("reviewer_stay_date"),
    expr("get_json_object(value, '$.reviewer_trip_type')").alias("reviewer_trip_type"),
    sentiment_udf("reviewer_comment").cast("float").alias("sentiment_score")
)

# Convert the string to an integer
format_df = format_df.withColumn("total_hotel_reviews", regexp_replace(col("total_hotel_reviews"), ",", "").cast("integer"))

# Remove the first character "đ" from the "price" column
format_df = format_df.withColumn("price", expr("substring(price, 2)"))
format_df = format_df.withColumn("price", regexp_replace(col("price"), ",", "").cast("integer"))

# Extract the reviewer rating as a integer
format_df = format_df.withColumn("reviewer_rating", expr("substring(reviewer_rating, 25)").cast("integer"))

# Extract the last word from the "reviewer_trip_type" column
format_df = format_df.withColumn("reviewer_trip_type", element_at(split(col("reviewer_trip_type"), " "), -1))

# Extract the month and year from "reviewer_stay_date" starting from the 15th character
format_df = format_df.withColumn("reviewer_stay_date", expr("substring(reviewer_stay_date, 15)"))
# Convert "reviewer_stay_date" to date type
format_df = format_df.withColumn("reviewer_stay_date", to_date(col("reviewer_stay_date"), "MMMM yyyy"))

# Convert "review_date" to date type
format_df = format_df.withColumn("review_date", to_date(col("review_date")))


# Drop the intermediate columns
# format_df.select("reviewer_rating", "reviewer_trip_type", "reviewer_stay_date", "price").show(truncate=False)
# format_df.printSchema()
# joined_df.show(truncate=False)




csv_file = '/home/unique_hotel.csv'
csv_df = spark.read.csv(csv_file, header=True, inferSchema=True)
csv_df = csv_df.withColumnRenamed("City", "city").withColumnRenamed("Country", "country").withColumnRenamed("Hotel_id", "hotel_id")
joined_df = format_df.join(csv_df, format_df.hotel_url == csv_df.Hotel_url, "left").drop(csv_df.Hotel_url)
joined_df = joined_df.withColumn("inserted_date", (lit(datetime.now())))

joined_df.select("review_date", "reviewer_stay_date").show(truncate=False)
# joined_df.printSchema()

# Define the keyspace and table name
keyspace = "datn"
table = "hotel_data"

# Save the DataFrame to Cassandra
joined_df.write.format("org.apache.spark.sql.cassandra") \
    .options(table=table, keyspace=keyspace) \
    .mode("append") \
    .save()


# Stop the SparkSession
spark.stop()

# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1,com.datastax.spark:spark-cassandra-connector_2.12:3.3.0 /home/process_data.py

#  kafka-topics.sh --list --bootstrap-server kafka:9092 --list

