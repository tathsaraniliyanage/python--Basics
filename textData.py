# Your data that you want to save
data = [
    "Hello, this is line 1.",
    "This is line 2.",
    "And here is line 3."
]

# Saving the data to a text file
with open('output.txt', 'w') as file:
    for line in data:
        file.write(line + '\n')  # Write each item on a new line

print("Data has been written to output.txt")
