# file_operations.py

def read_file(file_path):
    """Reads the data from the specified CSV file and returns it as a list of rows."""
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:  # Ensure valid row structure
                data.append(parts)
    return data

def convert_date_to_tuple(date_str):
    """Converts a date string (DD-MM-YYYY) into a (year, month, day) tuple."""
    day, month, year = int(date_str[:2]), int(date_str[3:5]), int(date_str[6:])
    return year, month, day

def filter_data(data, start_date, end_date):
    """Filters the data based on the given start and end date."""
    start_tuple = convert_date_to_tuple(start_date)
    end_tuple = convert_date_to_tuple(end_date)

    filtered = []
    for row in data:
        row_date_tuple = convert_date_to_tuple(row[0])
        if start_tuple <= row_date_tuple <= end_tuple:
            filtered.append(row)
    return filtered

def input_date(prompt):
    """Validates and returns a date input from the user."""
    while True:
        date = input(f"{prompt} (DD-MM-YYYY): ")
        if len(date) == 10 and date[2] == '-' and date[5] == '-':
            return date
        print("Invalid format. Please enter date as DD-MM-YYYY.")
