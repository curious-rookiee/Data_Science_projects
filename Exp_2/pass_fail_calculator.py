# pass_fail_calculator.py

# Function to calculate pass/fail status based on average marks
def calculate_pass_fail(csv_data, math_marks_index, english_marks_index):
    pass_count = 0
    fail_count = 0

    for row in csv_data:
        # Extract Math and English marks from respective indices
        math_mark = float(row[math_marks_index])
        english_mark = float(row[english_marks_index])

        # Calculate average marks
        avg_marks = (math_mark + english_mark) / 2

        # Determine pass or fail
        if avg_marks >= 40:
            # Adjusted to include students with exactly 40 marks as pass
            pass_count += 1
        else:
            fail_count += 1

    return pass_count, fail_count
