import os
import json
import csv
from AdjacencyList_DiGraph import DiGraph
from Algorithms import Haversine
from FlightRoute import FlightRoute
from Airport import Airport
from bst import bst


# Parse flight routes into an adjacency list, based on data from asia flight routes json file
# returns adjacency list
def ParseToAdjList(airportsBST) -> DiGraph:
    routesList = ParseRoutes(airportsBST)
    
    adjListGraph = DiGraph(routesList)

    return adjListGraph
    

# Reads routes csv file and makes flight route objects then append to list
# returns list of flight route objects
def ParseRoutes(airportsBST):
    routes_csv = os.getcwd() + "\\datasets\\routes.csv"
    routesList = []
    
    try:
        with open(routes_csv, 'r', encoding="utf_8") as routesFile:
            csvReader = csv.reader(routesFile)
            next(csvReader) # skip header row
            
            for row in csvReader:
                srcAirportCode = row[2]
                destAirportCode = row[4]
                srcAirportObj = airportsBST.get(srcAirportCode)
                destAirportObj = airportsBST.get(destAirportCode)
                if srcAirportObj is None or destAirportObj is None:
                    continue
                else:
                    distance = Haversine(srcAirportObj.longitude, srcAirportObj.latitude, destAirportObj.longitude, destAirportObj.latitude) 
                    flightRoute = FlightRoute(row[0], row[2], row[4], distance)
                    routesList.append(flightRoute)
                
    except Exception as e:
        print(e)
        
    return routesList
    

# Reads asia airports json file and loads data into a dictionary
# returns airports dictionary
def ParseAirports() -> dict:
    airports_json = os.getcwd() + "\\datasets\\airports.json"

    try:
        with open(airports_json, "r", encoding="utf_8") as airportsFile:
            airports_dict = json.load(airportsFile)
    except Exception as e:
        print(e)
        
    return airports_dict


# converts airports csv data into a binary search tree of nodes with airport IATA code as key and corresponding airport object as value
def create_airport_bst():
    # Open the CSV file and read the data
    with open(os.getcwd() + "\\datasets\\airports.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = [row for row in reader]
     
    bstReadyDict = {}
    
    for row in data:
        bstReadyDict[row[4]] = (Airport(row[0], row[1], row[2], row[3], row[4], row[5], float(row[6]), float(row[7])))
        
    bstOfAirports = bst()
    bstOfAirports.createBalancedTree(bstReadyDict)
    
    return bstOfAirports
