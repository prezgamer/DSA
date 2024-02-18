import csv
import os
from encodings import utf_8

airports_csv = os.getcwd() + "\\airports.csv"
asia_airports_csv = os.getcwd() + "\\AsiaAirports.csv"

try:
    rows = []
    
    with open(airports_csv, "r", encoding="utf_8") as file:
        csvReader = csv.reader(file)    
        for row in csvReader:
            # can add more conditions to cut airport dataset size
            if row[4].__contains__("\\N"):
                continue
            elif row[11].__contains__("Asia"):
                rows.append(row)

    with open(asia_airports_csv, "w", newline="", encoding="utf_8") as newFile:
        csvWriter = csv.writer(newFile)
        csvWriter.writerows(rows)
            
except Exception as e:
    print(e)