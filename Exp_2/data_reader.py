# data_reader.py

# Function to read CSV data without using any library
def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        # Read the header row
        header = file.readline().strip().split(',')

        # Read subsequent rows
        for line in file:
            # Remove any leading/trailing whitespace and split by comma
            fields = line.strip().split(',')
            data.append(fields)

    return header, data
