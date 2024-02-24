import dis
import json
import os

from networkx import desargues_graph
from numpy import double
# import networkx as nx
# import matplotlib.pyplot as plt

from DataParser import AirportsDictToList, ParseAirports, ParseRoutes, ParseToMatrix, RoutesDictToList
from Haversine import haversine

def main():
    # routesDict = ParseRoutes()
    airportsDict = ParseAirports()
    
    # routesList = RoutesDictToList(routesDict)
    airportsList = AirportsDictToList(airportsDict)
    
    sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
    destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
    
    airportsExists = validateChoices(sourceAirportCode, destAirportCode, airportsList)
    
    while (airportsExists == False):
        print("The airport codes you entered were invalid. Please enter again.")
        sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
        destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
        airportsExists = validateChoices(sourceAirportCode, destAirportCode, airportsList)
    
    for airport in airportsDict:
        if airport['IATA'] == sourceAirportCode:
            sourceAirport = airport
        elif airport['IATA'] == destAirportCode:
            destAirport = airport
    
    sourceLongitude = double(sourceAirport['longitude'])
    sourceLatitude = double(sourceAirport['latitude'])
    destLongitude = double(destAirport['longitude'])
    destLatitude = double(destAirport['latitude'])
    distance = haversine(sourceLongitude, sourceLatitude, destLongitude, destLatitude)
    print("The distance between the two airports chosen is: {:.2f}Km".format(distance))
            
    
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
            
    
def validateChoices(source, dest, airportsList):
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
    
    
if __name__ == "__main__":
    main()