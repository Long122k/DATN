# Use an appropriate base image with Python installed
FROM python:3.8

# Set the working directory in the container
WORKDIR /hotel_link

# Copy the contents of the tripAdvisor folder to the working directory in the container
COPY . .

# Install any required dependencies
RUN pip install -r requirements.txt

# Set the entry point command to run your Python script
CMD ["python3", "feed_urls_to_redis.py"]
