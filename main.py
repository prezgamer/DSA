import dis
from distutils.errors import LibError
import json
import os
from Airport import Airport
#from networkx import desargues_graph
#from numpy import double
# import networkx as nx
# import matplotlib.pyplot as plt
from DataParser import ParseRoutes, ParseAirports, RoutesDictToList, AirportsDictToList, ParseToAdjList
from Algorithms import Haversine, Dijkstra
from FlightRoute import FlightRoute


def main():
    adjListGraph = ParseToAdjList()
    adjListGraph.printAdjList("SIN")



def FindDistance():
    routesDict = ParseRoutes()
    airportsDict = ParseAirports()
    
    routesList = RoutesDictToList(routesDict)
    airportsList = AirportsDictToList(airportsDict)
    
    sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
    destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
    
    # if airports exists, returns pair of valid Airport objects and assigns to airportExists, else airportExists = None
    airportsExists = validateAirportChoice(sourceAirportCode, destAirportCode, airportsList)
    while (airportsExists == None):
        print("The airport codes you entered were invalid. Please enter again.")
        sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
        destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
        airportsExists = validateAirportChoice(sourceAirportCode, destAirportCode, airportsList)
    
    # if route exists, returns valid FlightRoute object and assigns to routeExists, else routeExists = None
    routeExists = validateRoute(sourceAirportCode, destAirportCode, routesList)
    while (routeExists == None):
        print("The flight route between your chosen airports does not exist. Please enter again.")
        # call function to get connecting routes here, using dijkstra algorithm to find shortest path from source to destination 
        sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
        destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
        airportsExists = validateAirportChoice(sourceAirportCode, destAirportCode, airportsList)
        routeExists = validateRoute(sourceAirportCode, destAirportCode, routesList)
    x
    sourceLongitude = float(airportsExists[0].getLongitude())
    sourceLatitude = float(airportsExists[0].getLatitude())
    destLongitude = float(airportsExists[1].getLongitude())
    destLatitude = float(airportsExists[1].getLatitude())
    distance = Haversine(sourceLongitude, sourceLatitude, destLongitude, destLatitude)
    print("The distance between the two airports chosen is: {:.2f}Km".format(distance))

    
def validateAirportChoice(sourceAirportCode, destAirportCode, airportsList) -> list[Airport] | None:
    sourceExists = False
    destExists = False
    
    for airport in airportsList:
        if airport.getIATA() == sourceAirportCode:
            sourceExists = True
            sourceAirport = airport
        elif airport.getIATA() == destAirportCode:
            destExists = True
            destinationAirport = airport
        if (sourceExists == False or destExists == False):
            continue
        else:
            return [sourceAirport, destinationAirport]
    
    return None    


def validateRoute(source, dest, routesList) -> FlightRoute | None:
    sourceExists = False
    destExists = False
    
    for route in routesList:
        if route.getSource() == source:
            sourceExists = True
        elif route.getDestination() == dest:
            destExists = True
        if (sourceExists == False or destExists == False):
            continue
        else:
            return route
        
    return None
                
    
if __name__ == "__main__":
    main()


# adjMatrix = ParseToMatrix()
# N = len(adjMatrix)
# G = nx.DiGraph()
# for i in range(N):
#     for j in range(N):
#         if adjMatrix[i][j] == 1:
#             G.add_edge(i,j)
# nx.draw(G, with_labels=True, node_color="lightblue", node_size=200, font_weight="bold")

# WARNING: very laggy, takes a while to start the interactive display
# plt.show()