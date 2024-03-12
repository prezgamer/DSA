import os
import json
from AdjacencyList import Graph
from FlightRoute import FlightRoute
from Airport import Airport

# Parse flight routes into an adjacency list, based on data from asia flight routes json file
# returns adjacency list
def ParseToAdjList() -> Graph:
    routes_dict = ParseRoutes()
    
    routesList = RoutesDictToList(routes_dict)
    
    adjListGraph = Graph(routesList)

    return adjListGraph
    

# Parse flight routes into an adjacency matrix, based on data from asia flight routes json file
# returns adjacency matrix
def ParseToMatrix() -> list[list[int]]:
    routes_dict = ParseRoutes()
    
    airports_dict = ParseAirports()
    
    routesList = RoutesDictToList(routes_dict)
    
    airportsList = AirportsDictToList(airports_dict)
    
    airportIndex = dict()
        
    # populate an index dictionary for airport codes
    for i in range(len(airportsList)):
        airportIndex[airportsList[i]] = i
    
    # initialize a 2D array of size N, N = number of Asia airports
    N = len(airportsList)
    adjMatrix = [[0 for i in range(N)] for j in range(N)]
    
    # for each route's source and destination, get it's corresponding index number
    # then populate 2D square array (adjacency matrix) using row and col index
    for routes in routesList:
        row = airportIndex[routes.getSource]
        col = airportIndex[routes.getDestination]
        adjMatrix[row][col] = 1
        
    return adjMatrix


# Reads asia routes json file and loads data into a dictionary
# returns routes dictionary
def ParseRoutes() -> dict:
    routes_json = os.getcwd() + "\\datasets\\AsiaRoutes.json"
    
    try:
        with open(routes_json, 'r', encoding="utf_8") as routesFile:
            routes_dict = json.load(routesFile)
    except Exception as e:
        print(e)
        
    return routes_dict
    

# Reads asia airports json file and loads data into a dictionary
# returns airports dictionary
def ParseAirports() -> dict:
    airports_json = os.getcwd() + "\\datasets\\AsiaAirports.json"

    try:
        with open(airports_json, "r", encoding="utf_8") as airportsFile:
            airports_dict = json.load(airportsFile)
    except Exception as e:
        print(e)
        
    return airports_dict

# converts routes dictionary into a list of FlightRoute objects
# returns list of FlightRoute objects
def RoutesDictToList(routesDict) -> list[FlightRoute]:
    routesList = []
    
    # for every route object, parse into pairs of source and destination airports
    for routes in routesDict:
        route = FlightRoute(routes['airline'],routes['sourceAirport'], routes['destAirport'], routes['distance'])
        routesList.append(route)
        
    return routesList

# converts airports dictionary into a list of Airport objects
# returns list of Airport objects
def AirportsDictToList(airportsDict) -> list[Airport]:
    airportsList = []
    
    # for every airport object, parse into list of airport codes and sort alphabetically
    for airports in airportsDict:
        airport = Airport(airports['airportName'], airports['city'], airports['country'], airports['IATA'], airports['latitude'], airports['longitude'])
        airportsList.append(airport)
    
    return airportsList