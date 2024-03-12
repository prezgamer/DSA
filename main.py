import dis
import json
import os
#from networkx import desargues_graph
#from numpy import double
# import networkx as nx
# import matplotlib.pyplot as plt
from DataParser import ParseRoutes, ParseAirports, RoutesDictToList, AirportsDictToList, ParseToAdjList
from Algorithms import Haversine, Dijkstra


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
    
    airportsExists = validateAirportChoice(sourceAirportCode, destAirportCode, airportsList)
    while (airportsExists == False):
        print("The airport codes you entered were invalid. Please enter again.")
        sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
        destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
        airportsExists = validateAirportChoice(sourceAirportCode, destAirportCode, airportsList)
    
    routeExists = validateRoute(sourceAirportCode, destAirportCode, routesList)
    while (routeExists == False):
        print("The flight between your chosen airports does not exist. Please enter again.")
        sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
        destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
        airportsExists = validateAirportChoice(sourceAirportCode, destAirportCode, airportsList)
        routeExists = validateRoute(sourceAirportCode, destAirportCode, routesList)

    for airport in airportsDict:
        if airport['IATA'] == sourceAirportCode:
            sourceAirport = airport
        elif airport['IATA'] == destAirportCode:
            destAirport = airport
    
    sourceLongitude = float(sourceAirport['longitude'])
    sourceLatitude = float(sourceAirport['latitude'])
    destLongitude = float(destAirport['longitude'])
    destLatitude = float(destAirport['latitude'])
    distance = Haversine(sourceLongitude, sourceLatitude, destLongitude, destLatitude)
    print("The distance between the two airports chosen is: {:.2f}Km".format(distance))

    
def validateAirportChoice(source, dest, airportsList):
    sourceExists = False
    destExists = False
    
    for airport in airportsList:
        if airport == source:
            sourceExists = True
        elif airport == dest:
            destExists = True
                
    if (sourceExists == False or destExists == False):
        return False
    else:
        return True
    

def validateRoute(source, dest, routesList):
    sourceExists = False
    destExists = False
    
    for route in routesList:
        if route[0] == source:
            sourceExists = True
        elif route[1] == dest:
            destExists = True
                
    if (sourceExists == False or destExists == False):
        return False
    else:
        return True
    
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