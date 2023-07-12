import csv

city_intro = []
error = []
modified_link = 'https://www.tripadvisor.com/'
with open('./link_city.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        row[-1] = modified_link + row[-1].replace("Hotels","Tourism" ).replace( "Hotels", "Vacations")
        # print(row[1])
        # print(row[-1])
        if row[1] in row[-1]:
            city_intro.append(row)
        else:
            error.append(row)
        # print(city_intro)
        # print(error)
        # break

with open('./link_city_intro.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['City_id', 'City_name', 'Country_name', 'Link'])
    for link in city_intro:
            writer.writerow(link)
    f.close()

with open('./error_city.csv', 'w', newline='') as f1:
    writer1 = csv.writer(f1)
    writer1.writerow(['City_id', 'City_name', 'Country_name', 'Link'])
    for link in error:
            writer1.writerow(link)
    f1.close()