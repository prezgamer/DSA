import csv
import os

routes_csv = os.getcwd() + "\\routes.csv"
asiaAirportsCSV = os.getcwd() + "\\AsiaAirports.csv"
asiaRoutesCSV = os.getcwd() + "\\AsiaRoutes.csv"

try:
    asiaCodes = []

    with open(asiaAirportsCSV, "r", encoding="utf_8") as asiaAirportFile:
        csvReader = csv.reader(asiaAirportFile)
        for row in csvReader:
            asiaCodes.append(row[4])
    
    with open(routes_csv, "r", encoding="utf_8") as routesFile:
        with open(asiaRoutesCSV, "w", newline="", encoding="utf_8") as asiaRoutesFile:
            csvReader = csv.reader(routesFile)
            csvWriter = csv.writer(asiaRoutesFile)
            
            for route in csvReader:
                for country in asiaCodes:
                    if route[2] == country:
                        csvWriter.writerow(route)
                        # break out of inner for-loop because once a row has been identified with an asian country code, no need to check anymore
                        break
                
except Exception as e:
    print(e)