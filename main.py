# import json
# import os
# print(os.getcwd())

# # Define the file name
# file_name = open("C:/Users/ffjan/OneDrive/Desktop/DSA Project/DSA/Routes.json")

# # returns JSON object as 
# # a dictionary
# data = json.load(file_name)
 
# # Iterating through the json
# # list
# for i in data["AirlineDetails"]:
#     print(i)

import json
import os
print(os.getcwd())

file_name = 'C:/Users/ffjan/OneDrive/Desktop/DSA Project/Routes.json'
print(file_name)

try:
    # Open the file in read mode
    with open(file_name, "r") as file:
        # Read the contents of the file
        routes_data = json.load(file)
        print(routes_data)
except Exception as e:
    print("Error loading JSON file:", e)

# try:
#     # Open the file in read mode
#     with open('Routes.json', 'r', encoding='utf-8') as file:
#         # Read the contents of the file
#         routes_data = json.load(file)
#         print(routes_data)

# except FileNotFoundError:
#     print(f"File '{'C:/Users/ffjan/OneDrive/Desktop/DSA Project/DSA/Routes.json'}' not found.")
# except json.JSONDecodeError as e:
#     print(f"Error decoding JSON file '{'C:/Users/ffjan/OneDrive/Desktop/DSA Project/DSA/Routes.json'}': {e}")
# except Exception as e:
#     print(f"Error loading JSON file '{'C:/Users/ffjan/OneDrive/Desktop/DSA Project/DSA/Routes.json'}': {e}")