import os
import csv
from Algorithms import Haversine
from DataParser import AirportsDictToList, ParseAirports
"""
Calculates the distance for each flight route in asia, and write to file.
Only used once, information is saved to file.
"""
def RouteWeight():
    asiaRoutesCSV = os.getcwd() + "\\datasets\\AsiaRoutes.csv"
    newRoutesCSV = os.getcwd() + "\\datasets\\AsiaRoutes2.csv"
    
    airportsDict = ParseAirports()
    airportsList = AirportsDictToList(airportsDict)
    
    routeRows = []
    
    try:
        with open(asiaRoutesCSV, "r", encoding="utf_8") as asiaRoutesFile:
            with open(newRoutesCSV, "w", newline= "", encoding="utf_8") as newRoutesFile:
                csvReader = csv.reader(asiaRoutesFile)
                csvWriter = csv.writer(newRoutesFile)

                for route in csvReader:
                    # first line checker, skips processing column headers after writing them to new file
                    if route[2] == "sourceAirport":
                        csvWriter.writerow(route)
                        continue
                    sourceAirportCode = route[2]
                    destAirportCode = route[4]
                    for airport in airportsList:
                        if airport.getIATA() == sourceAirportCode:
                            sourceAirport = airport
                        elif airport.getIATA() == destAirportCode:
                            destinationAirport = airport
                    distance = Haversine(float(sourceAirport.getLongitude()), float(sourceAirport.getLatitude()), float(destinationAirport.getLongitude()), float(destinationAirport.getLatitude()))
                    route.append(str(distance))
                    print(route)
                    csvWriter.writerow(route)
                
    except Exception as e:
        print(e)
        

RouteWeight()