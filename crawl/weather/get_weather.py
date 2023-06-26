import requests
import json
import csv
from datetime import datetime, timedelta
import time

# API endpoint
url = "https://archive-api.open-meteo.com/v1/archive"

input_file = "./crawl/city.csv"
output_file_name = "./crawl/weather1.json"

# Read parameter values from the CSV file
parameters = []
with open(input_file, "r") as input_file:
    csv_reader = csv.DictReader(input_file)
    for row in csv_reader:
        parameters.append(row)


# Calculate start_date and end_date based on the current date
current_date = datetime.now()
start_date = (current_date - timedelta(days=10)).strftime("%Y-%m-%d")
end_date = (current_date - timedelta(days=9)).strftime("%Y-%m-%d")
i = 0
list_data = {}
session = requests.Session()
# Open the CSV file for writing
with open(output_file_name, "w") as output_file:

    # Iterate through each set of parameters and send API requests
    for params in parameters:
        latitude = params["latitude"]
        longitude = params["longitude"]
        # Construct the API request URL with the dynamic parameters
        api_params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": start_date,
            "end_date": end_date,
            "hourly": "temperature_2m,relativehumidity_2m,apparent_temperature,rain,snowfall",
            "timezone": "Asia/Bangkok"
        }

        # Send the API request
        response = session.get(url, params=api_params)
        data = response.json()
        list_data[i] = data
        i = i+1
        print(i)
        break
        # time.sleep(2)
    session.close()
    # Write the data to a CSV file
    with open(output_file_name, "w", encoding="utf-8") as file:
        json.dump(list_data, file,ensure_ascii=False)

    
print("Data has been successfully stored in", output_file)
