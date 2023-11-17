def find_common_lines(file1, file2, output_file):
    # Open the files in read mode
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Create a set to store lines from file1
        lines_set = set()

        # Read lines from file1 and store them in the set
        for line in f1:
            lines_set.add(line.strip())

        # Open the output file in write mode
        with open(output_file, 'w') as output:
            # Read lines from file2 and check if they are in the set
            for line in f2:
                if line.strip() in lines_set:
                    # If the line is in both files, write it to the output file
                    output.write(line)

# Example usage
file1_path = 'file1.txt'
file2_path = 'file2.txt'
output_file_path = 'common_lines_output.txt'

find_common_lines(file1_path, file2_path, output_file_path)
