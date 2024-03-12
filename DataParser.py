import os
import json
from AdjacencyList import Graph
from FlightRoute import FlightRoute
from Airport import Airport


# parse airports into adjacency list based on existing flight routes
def ParseToAdjList() -> Graph:
    routes_dict = ParseRoutes()
    
    routesList = RoutesDictToList(routes_dict)
    
    adjListGraph = Graph(routesList)

    return adjListGraph
    

# Parse airports into an adjacency matrix based on existing flight routes
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

        
def ParseRoutes() -> dict:
    routes_json = os.getcwd() + "\\datasets\\AsiaRoutes.json"
    
    try:
        with open(routes_json, 'r', encoding="utf_8") as routesFile:
            routes_dict = json.load(routesFile)
    except Exception as e:
        print(e)
        
    return routes_dict
    
    
def ParseAirports() -> dict:
    airports_json = os.getcwd() + "\\datasets\\AsiaAirports.json"

    try:
        with open(airports_json, "r", encoding="utf_8") as airportsFile:
            airports_dict = json.load(airportsFile)
    except Exception as e:
        print(e)
        
    return airports_dict


def RoutesDictToList(routesDict) -> list[FlightRoute]:
    routesList = []
    
    # for every route object, parse into pairs of source and destination airports
    for routes in routesDict:
        route = FlightRoute(routes['airline'],routes['sourceAirport'], routes['destAirport'], routes['distance'])
        routesList.append(route)
        
    return routesList


def AirportsDictToList(airportsDict) -> list[Airport]:
    airportsList = []
    
    # for every airport object, parse into list of airport codes and sort alphabetically
    for airports in airportsDict:
        airport = Airport(airports['airportName'], airports['city'], airports['country'], airports['IATA'], airports['latitude'], airports['longitude'])
        airportsList.append(airport)
    
    return airportsList