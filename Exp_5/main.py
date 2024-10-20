# main.py

from operation import read_file, filter_data, input_date
from calculation import (average_calories_per_day, highest_calories_per_day,
                          calculate_standard_deviation, highest_calories,
                          overall_average_calories)

def main():
    """Main function to execute the program."""
    file_path = 'dates_values.csv'
    data = read_file(file_path)

    start_date = input_date("From Date")
    end_date = input_date("To Date")

    filtered_data = filter_data(data, start_date, end_date)

    # Display the results
    avg_per_day = average_calories_per_day(filtered_data)
    max_per_day = highest_calories_per_day(filtered_data)
    std_dev = calculate_standard_deviation(filtered_data)
    max_cal_in_range = highest_calories(filtered_data)
    overall_avg = overall_average_calories(filtered_data)

    print(f"\nData from {start_date} to {end_date}:")
    for date, avg in avg_per_day.items():
        print(f"Date: {date}, Average Calories: {avg:.2f}")

    for date, max_cal in max_per_day.items():
        print(f"Date: {date}, Highest Calories: {max_cal}")

    if std_dev is not None:
        print(f"Standard Deviation: {std_dev:.2f}")

    if max_cal_in_range is not None:
        print(f"Highest Calories in Range: {max_cal_in_range}")

    if overall_avg is not None:
        print(f"Overall Average Calories: {overall_avg:.2f}")
    else:
        print("No data available.")

if __name__ == "__main__":
    main()
