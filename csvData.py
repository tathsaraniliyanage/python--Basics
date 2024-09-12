import csv

# Writing data to a CSV file
data = [["Name", "Age", "City"], ["Alice", 30, "New York"], ["Bob", 25, "Los Angeles"]]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
