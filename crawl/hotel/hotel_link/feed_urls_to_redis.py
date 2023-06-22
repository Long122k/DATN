import csv
import redis

redis_host = 'redis_queue'  # Replace with your Redis server hostname or IP address
redis_port = 6379  # Replace with the Redis server port
r = redis.Redis(host=redis_host, port=redis_port)
with open('./tripAdvisor/unique_hotels.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        url = row[1]  # Assuming the URL is in the first column of the CSV file
        r.lpush('url_queue', url)  # Push the URL to the Redis queue
r.close()
    