import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Read data from the file
    with open(t, 'r') as file:
        snowfall_data = [float(line.strip()) for line in file if line.strip()]

    # Aggregate data into 10 cm ranges
    range_counts = {}
    for snowfall in snowfall_data:
        range_start = int(snowfall // 10) * 10
        range_end = range_start + 10

        # Update the count for the corresponding range
        key = f"{range_start}-{range_end}"
        range_counts[key] = range_counts.get(key, 0) + 1

    # Extract x and y values for the bar chart
    ranges, counts = zip(*sorted(range_counts.items()))

    # Plotting the bar graph
    plt.bar(ranges, counts, color='blue')
    plt.xlabel('Snowfall Range (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.show()
    plt.savefig('snowfall.png')
    
# Example usage:
graphSnowfall('snowfall_data.txt')
