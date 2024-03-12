import csv
import os
"""
Cut out fight routes that don't involve airports in Asia, only write to file routes within Asia
Used only once.
"""
def TrimRoutes():
    routes_csv = os.getcwd() + "\\datasets\\routes.csv"
    asiaAirportsCSV = os.getcwd() + "\\datasets\\AsiaAirports.csv"
    asiaRoutesCSV = os.getcwd() + "\\datasets\\AsiaRoutes.csv"

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
                    for airport in asiaCodes:
                        if route[2] == airport:
                            for airport in asiaCodes:
                                if route[4] == airport:
                                    csvWriter.writerow(route)
                    
    except Exception as e:
        print(e)