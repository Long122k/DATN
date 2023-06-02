import csv

filename = "crawl/flight/iata-icao.csv"  # Replace with the actual filename or path
output_filename = "crawl/flight/icao.csv"
def getIcao(filename, output_filename):
    icao_list = []  # List to store the extracted data

    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists

        for row in csv_reader:
            icao = row[3]  # Assuming "icao" is the fourth column (index 3)
            if icao != "":
                icao_list.append(icao)
    # # Print the extracted data
    # for icao in icao_list:
    #     print(icao)
    # Write the extracted data to a new CSV file
    with open(output_filename, "w", newline="") as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(["icao"])  # Write the header row

        for icao in icao_list:
            csv_writer.writerow([icao])
getIcao(filename, output_filename)
# 1514764800
# 1515196800