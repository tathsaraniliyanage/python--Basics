import pickle

# Saving data to a pickle file
data = {"Name": "Alice", "Age": 30, "City": "New York"}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
