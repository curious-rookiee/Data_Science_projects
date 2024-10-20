# calculations.py

def average_calories_per_day(filtered_data):
    """Calculates the average calories per day."""
    daily_totals = {}
    for date, calories in filtered_data:
        if date not in daily_totals:
            daily_totals[date] = []
        daily_totals[date].append(int(calories))

    averages = {}
    for date, cal_list in daily_totals.items():
        averages[date] = sum(cal_list) / len(cal_list)
    return averages

def overall_average_calories(filtered_data):
    """Calculates the overall average calories in the selected range."""
    total, count = 0, 0
    for _, calories in filtered_data:
        total += int(calories)
        count += 1

    return total / count if count else None

def highest_calories(filtered_data):
    """Finds the highest calories value in the filtered data."""
    max_cal = 0
    for _, calories in filtered_data:
        cal_value = int(calories)
        if cal_value > max_cal:
            max_cal = cal_value
    return max_cal

def calculate_standard_deviation(filtered_data):
    """Calculates the standard deviation of the calories."""
    calories = [int(row[1]) for row in filtered_data]
    if len(calories) < 2:
        return None

    mean = sum(calories) / len(calories)
    variance = sum((x - mean) ** 2 for x in calories) / len(calories)
    return variance ** 0.5

def highest_calories_per_day(filtered_data):
    """Finds the highest calories value for each day."""
    daily_max = {}
    for date, calories in filtered_data:
        cal_value = int(calories)
        if date not in daily_max or cal_value > daily_max[date]:
            daily_max[date] = cal_value
    return daily_max
