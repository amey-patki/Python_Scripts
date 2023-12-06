import csv

# Function to read from the Address table and print to a file
def read_from_address_table(output_file):
    # Simulating reading from the Address table
    address_data = [
        {'ID': '1', 'Name': 'Name1', 'Address': 'add1', 'City': 'Mumbai'},
        {'ID': '2', 'Name': 'Name2', 'Address': 'add2', 'City': 'Bangalore'},
        {'ID': '3', 'Name': 'Name3', 'Address': 'add3', 'City': 'Coimbatore'},
        # Add more data as needed
    ]

    # Write the data to the output file
    with open(output_file, 'w', newline='') as output:
        fieldnames = ['ID', 'Name', 'Address', 'City']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(address_data)

# Function to append contents of address.txt to new_data.txt
def append_to_new_data(input_file, output_file):
    # Read data from the input file
    with open(input_file, 'r') as input_csv:
        reader = csv.DictReader(input_csv)

        # Append the data to the existing file
        with open(output_file, 'a', newline='') as output:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writerows(reader)

# Example usage
new_data_file_path = 'new_data.txt'
address_file_path = 'address.txt'

#  Read from the Address table and print to new_data.txt
read_from_address_table(new_data_file_path)

# Part b: Append contents of address.txt to new_data.txt
append_to_new_data(address_file_path, new_data_file_path)
