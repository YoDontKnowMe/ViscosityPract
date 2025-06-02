import matplotlib.pyplot as plt

FILE_PATH = "./RESULTS/"
LETTER = input("What file? ")

def read_file(file_path):
    time = []
    y_meters = []
    with open(file_path, 'r') as file:
        lines = file.readlines()[2:]  # Skip the first two lines
        for line in lines:
            data = line.strip().split(',')
            if len(data) >= 2:  # Ensure there are at least two columns
                time.append(float(data[0]))  # TIME column
                y_meters.append(float(data[1]))  # Y column
    return time, y_meters

# File paths
file1 = FILE_PATH + LETTER + '1.txt'
file2 = FILE_PATH + LETTER + '2.txt'
file3 = FILE_PATH + LETTER + '3.txt'

# Read data from files
time1, y1 = read_file(file1)
time2, y2 = read_file(file2)
time3, y3 = read_file(file3)

# print(y1)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time1, y1, label='File 1')
plt.plot(time2, y2, label='File 2')
plt.plot(time3, y3, label='File 3')
# Calculate speeds (dy/dt) for each file
speed1 = [(y1[i+1] - y1[i]) / (time1[i+1] - time1[i]) for i in range(len(time1) - 1)]
speed2 = [(y2[i+1] - y2[i]) / (time2[i+1] - time2[i]) for i in range(len(time2) - 1)]
speed3 = [(y3[i+1] - y3[i]) / (time3[i+1] - time3[i]) for i in range(len(time3) - 1)]

# Calculate average speeds with higher precision
avg_speed1 = round(sum(speed1) / len(speed1), 6)
avg_speed2 = round(sum(speed2) / len(speed2), 6)
avg_speed3 = round(sum(speed3) / len(speed3), 6)

# Calculate overall average speed with higher precision
overall_avg_speed = round((avg_speed1 + avg_speed2 + avg_speed3) / 3, 6)

# Print average speeds
# Write averages to a file
output_file = FILE_PATH + LETTER + '_avg.txt'
with open(output_file, 'w') as file:
    file.write(f"Average Speed for File 1: {avg_speed1:.6f} meters/second\n")
    file.write(f"Average Speed for File 2: {avg_speed2:.6f} meters/second\n")
    file.write(f"Average Speed for File 3: {avg_speed3:.6f} meters/second\n")
    file.write(f"Overall Average Speed: {overall_avg_speed:.6f} meters/second\n")

# Print confirmation
print(f"Averages written to {output_file}")

file_name = "WRONG"

match LETTER:
    case 'a':
        file_name = "Buis A"
    case 'b':
        file_name = "Buis B"
    case 'c':
        file_name = "Buis C"
    case 'w':
        file_name = "Water"
    case _:
        print("No file selected.")

# Customize the graph
plt.xlabel('Time (s)')
plt.ylabel('Y (meters)')
plt.title('Grafiek van de ' + file_name + ' Files')
plt.legend()
plt.grid(True)

# Save the graph as an image
graph_file = FILE_PATH + LETTER + '_graph.png'
plt.savefig(graph_file)
print(f"Graph saved as {graph_file}")

# Show the graph
plt.show()