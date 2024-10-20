
from data_reader import read_csv_file
from pass_fail_calculator import calculate_pass_fail
from plotter import plot_pass_fail_distribution, plot_gender_distribution

# Example usage to read CSV file
file_path = 'marks.csv'

header, csv_data = read_csv_file(file_path)

# Find the indices of 'MATH MARKS' and 'ENGLISH MARKS' in header
math_marks_index = header.index('Math Marks')
english_marks_index = header.index('English Marks')

# Calculate pass/fail counts based on average marks
pass_count, fail_count = calculate_pass_fail(csv_data, math_marks_index, english_marks_index)

# Extract gender column data
gender_index = header.index('Gender')
genders = [row[gender_index] for row in csv_data]

# Plot the distributions
plot_pass_fail_distribution(pass_count, fail_count)
plot_gender_distribution(genders)
