# Use the base Spark image
FROM bitnami/spark:3.4

# Set the working directory
WORKDIR /opt/bitnami/spark

# Install vaderSentiment
RUN pip install vaderSentiment

# Copy your Spark script to the container
COPY . /home/

# Set the entry point
# ENTRYPOINT ["spark-submit", "process_data.py"]
