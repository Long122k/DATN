import csv
import aiohttp
import asyncio

# Function to translate city names to English
async def translate_city_name(session, city_name):
    async with session.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=en&dt=t&q={city_name}") as response:
        translation = await response.json()
        translated_city_name = translation[0][0][0]

        return translated_city_name

# Path to the CSV file
csv_file = '/home/dolong/Documents/Code/DATN/crawl/states.csv'
new_states = '/home/dolong/Documents/Code/DATN/crawl/new_states.csv'

# Read the CSV file
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

    # Remove quotation marks from the city name
    for row in rows:
        city_name = row[1]
        city_name = city_name.strip('"') + " province" # Remove quotation marks if present
        row[1] = city_name

# Perform translations asynchronously
async def translate_async():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for row in rows:
            city_name = row[1]
            tasks.append(asyncio.create_task(translate_city_name(session, city_name)))

        translations = await asyncio.gather(*tasks)

        # Update the translated city names in the rows
        for i, translation in enumerate(translations):
            rows[i][1] = translation[:-9]

# Run the asynchronous translation task
asyncio.run(translate_async())

# Write the modified data back to the CSV file
with open(new_states, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("City names have been translated and updated in the CSV file. Quotation marks have been removed.")
