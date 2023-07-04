import csv

def check_duplicates(csv_file, new_file):
    unique_rows = set()
    duplicate_rows = []
    wrong_hotel = 0
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        
        next(reader, None)
        
        for row in reader:
            #check if the hotel belong to right city
            address =  row[-1].split('-')[-1].split('.')[0].split('_')
            if all(element in address for element in row[0].split(' ')):
                # Convert the row to a tuple for efficient comparison
                row_tuple = tuple(row)
                
                if row_tuple in unique_rows:
                    duplicate_rows.append(row)
                else:
                    unique_rows.add(row_tuple)
            else:
                wrong_hotel = wrong_hotel + 1
        with open(new_file, 'w', newline='') as file1:
            csv_writer = csv.writer(file1)
            csv_writer.writerow(['City', 'Country', 'Hotel_id', 'Hotel_url'])
            csv_writer.writerows(unique_rows)
    return duplicate_rows, wrong_hotel

# Example usage
csv_file = 'crawl/hotel/hotel_link/tripAdvisor/hotel.csv'
new_file = 'crawl/hotel/hotel_link/tripAdvisor/unique_hotel.csv'
duplicates = check_duplicates(csv_file, new_file)

print((duplicates[1]))
if duplicates:
    print(f"Found {len(duplicates[0])} duplicate rows:")
    # for duplicate in duplicates:
    #     print(duplicate)
    print(len(duplicates[0]))
else:
    print("No duplicate rows found.")