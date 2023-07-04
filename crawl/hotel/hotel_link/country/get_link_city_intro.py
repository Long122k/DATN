import csv

city_intro = []
modified_link = 'https://www.tripadvisor.com/'
with open('./link_city.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        row[-1] = modified_link + row[-1].replace("Hotels","Tourism" ).replace( "Hotels", "Vacations")
        city_intro.append(row)

with open('./link_city_intro.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['City_id', 'City_name', 'Country_name', 'Link'])
    for link in city_intro:
            writer.writerow(link)
