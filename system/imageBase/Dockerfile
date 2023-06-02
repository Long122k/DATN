
FROM ubuntu:20.04

# Install Java
RUN apt-get update -y && \
    apt-get install -y wget && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y python3.8 && \
    apt-get install -y python3-pip && \
    pip install pyspark


# Install Spark
RUN wget -O spark.tgz https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz && \
    tar -xvzf spark.tgz && \
    mv spark-3.3.2-bin-hadoop3 /spark && \
    rm spark.tgz

# Install Hadoop
RUN wget -O hadoop.tar.gz https://archive.apache.org/dist/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz && \
    tar -xvzf hadoop.tar.gz && \
    mv hadoop-3.3.0 /hadoop && \
    rm hadoop.tar.gz

# Install Kafka
RUN apt-get install -y wget && \
    wget -O kafka.tgz https://archive.apache.org/dist/kafka/3.3.1/kafka_2.12-3.3.1.tgz && \
    tar -xvzf kafka.tgz && \
    mv kafka_2.12-3.3.1 /kafka && \
    rm kafka.tgz

# Set environment variables
ENV SPARK_HOME=/spark
ENV HADOOP_HOME=/hadoop
ENV KAFKA_HOME=/kafka

# Add Spark, Hadoop, and Kafka to the PATH
ENV PATH=$PATH:$SPARK_HOME/bin:$HADOOP_HOME/bin:$KAFKA_HOME/bin

# Define a volume for shared data
VOLUME /data

# Set the working directory
WORKDIR /data

# Default command upon container launch
CMD ["bash"]