import csv
from googletrans import Translator
import time
# Function to translate city names to English
def translate_city_name(city_name):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(city_name, dest='en')
    return translation.text

#Path to the CSV file
csv_file = '/home/dolong/Documents/Code/DATN/process/spark/world-cities.csv'
new_states = '/home/dolong/Documents/Code/DATN/process/spark/new_states.csv'

# Read the CSV file
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

    # Iterate through each row and translate the city name
    for row in rows:
        row[1] = row[1].strip('"')  # Remove quotation marks if present
        city_name = row[1] + " province"
        print(city_name)
        translated_city_name = translate_city_name(city_name)
        row[1] = translated_city_name
        time.sleep(3)

# Write the modified data back to the CSV file
with open(new_states, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("City names have been translated and updated in the CSV file.")
