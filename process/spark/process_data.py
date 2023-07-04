import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaSparkIntegration") \
    .master("local[1]") \
    .getOrCreate()

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
                expr("get_json_object(value, '$.star')").alias("star"),
                expr("get_json_object(value, '$.hotel_address')").alias("hotel_address"),
                expr("get_json_object(value, '$.price')").alias("price"),
                expr("get_json_object(value, '$.review_date')").alias("review_date"),
                expr("get_json_object(value, '$.reviewer_rating')").alias("reviewer_rating"),
                expr("get_json_object(value, '$.reviewer_contribution')").alias("reviewer_contribution"),
                expr("get_json_object(value, '$.reviewer_link')").alias("reviewer_link"),
                expr("get_json_object(value, '$.reviewer_title_comment')").alias("reviewer_title_comment"),
                expr("get_json_object(value, '$.reviewer_comment')").alias("reviewer_comment"),
                expr("get_json_object(value, '$.reviewer_stay_date')").alias("reviewer_stay_date"),
                expr("get_json_object(value, '$.reviewer_trip_type')").alias("reviewer_trip_type"),
                sentiment_udf("reviewer_comment").alias("sentiment_score")
)

csv_file= '/home/new_states.csv'
csv_df = spark.read.csv(csv_file, header=True, inferSchema=True)
joined_df = format_df.join(csv_df, format_df.hotel_url == csv_df.hotel_link, "left")



# Stop the SparkSession
spark.stop()

# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 /home/process_data.py
#  kafka-topics.sh --list --bootstrap-server kafka:9092 --list

