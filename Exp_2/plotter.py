# plotter.py

import matplotlib.pyplot as plt

def plot_pass_fail_distribution(pass_count, fail_count):
    # Plotting the pie chart for pass/fail distribution
    labels_pass_fail = ['Pass', 'Fail']
    sizes_pass_fail = [pass_count, fail_count]
    colors_pass_fail = ['lightgreen', 'lightcoral']
    explode_pass_fail = (0.1, 0)  # Explode the 'Pass' slice

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.pie(sizes_pass_fail, labels=labels_pass_fail, colors=colors_pass_fail, explode=explode_pass_fail, autopct='%1.1f%%', startangle=140)
    plt.title('Pass/Fail Distribution based on Average Marks')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

def plot_gender_distribution(genders):
    # Calculate counts for each gender
    gender_counts = {}
    for gender in genders:
        if gender in gender_counts:
            gender_counts[gender] += 1
        else:
            gender_counts[gender] = 1

    # Plotting the pie chart for gender distribution
    labels_gender = list(gender_counts.keys())
    sizes_gender = list(gender_counts.values())
    colors_gender = ['lightblue', 'pink']  # Adjust colors as needed

    plt.subplot(1, 2, 2)  # Rows and columns and plot number to specify the position of the plot
    plt.pie(sizes_gender, labels=labels_gender, colors=colors_gender, autopct='%1.1f%%', startangle=140)
    plt.title('Gender Distribution')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    plt.tight_layout()  # Ensures spacing between subplots
    plt.show()
