import csv

def check_duplicates(csv_file, new_file):
    unique_rows = set()
    duplicate_rows = []
    
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        
        header = next(reader, None)
        
        for row in reader:
            # Convert the row to a tuple for efficient comparison
            row_tuple = tuple(row)
            
            if row_tuple in unique_rows:
                duplicate_rows.append(row)
            else:
                unique_rows.add(row_tuple)

        with open(new_file, 'w', newline='') as file1:
            csv_writer = csv.writer(file1)
            csv_writer.writerow(['Hotel_id', 'Hotel_url'])
            csv_writer.writerows(unique_rows)
    return duplicate_rows

# Example usage
csv_file = 'crawl/hotel/tripAdvisor/tripAdvisor/hotels.csv'
new_file = 'crawl/hotel/tripAdvisor/tripAdvisor/unique_hotels.csv'
duplicates = check_duplicates(csv_file, new_file)

if duplicates:
    print(f"Found {len(duplicates)} duplicate rows:")
    for duplicate in duplicates:
        print(duplicate)
    print(len(duplicates))
else:
    print("No duplicate rows found.")