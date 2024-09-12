import json

# Saving data to a JSON file
data = {"Name": "Alice", "Age": 30, "City": "New York"}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
