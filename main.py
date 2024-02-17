import json

# Define the file name
file_name = "C:\Users\ffjan\OneDrive\Desktop\Python\DSA\Routes.json"

# Open the file in read mode
with open(file_name, "r") as file:
    # Read the contents of the file
    routes_data = json.load(file)

# Now you can work with the data loaded from the JSON file
# For example, you can print it
print(routes_data)