import csv

def sort_data_by_column(input_file, output_file, sort_column):
    # Read data from the input file
    with open(input_file, 'r') as input_csv:
        reader = csv.DictReader(input_csv)
        # Sort the data based on the specified column
        sorted_data = sorted(reader, key=lambda row: row['City'])

    # Write the sorted data to the output file
    with open(output_file, 'w', newline='') as output_csv:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_data)

# Example usage
input_file_path = 'Sample.csv'  # Replace with your actual input file path
output_file_path = 'sorted_data_by_column.csv'
sort_column_name = 'City'  # Replace with the column name you want to sort by

sort_data_by_column(input_file_path, output_file_path, sort_column_name)
