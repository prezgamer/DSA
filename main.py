from types import NoneType
from Airport import Airport
from DataParser import ParseRoutes, ParseAirports, RoutesDictToList, AirportsDictToList, ParseToAdjList
from Algorithms import Dijkstra
from FlightRoute import FlightRoute


def main(fromAirport: str,toAirport: str):
    adjListGraph = ParseToAdjList()
    
    start, end = getAirport(fromAirport, toAirport)
    
    if start is None or end is None:
        print("No such airports exist")
        raise Exception("No such airports exist")
    else:
        try:
            shortest_path, shortest_distance = Dijkstra(adjListGraph.getAdjList(), start['IATA'], end['IATA'])
            shortest_distance = '{:.2f}'.format(shortest_distance)
            
            print(f"The shortest path from {start['airportName']} to {end['airportName']} is: {shortest_path}")
            print(f"The shortest distance from {start['airportName']} to {end['airportName']} is: {shortest_distance}")
            
            fromAirportLatitude = start['latitude']
            fromAirportLongitude = start['longitude']
            toAirportLatitude = end['latitude']
            toAirportLongitude = end['longitude']

            return shortest_path, shortest_distance, fromAirportLatitude, fromAirportLongitude, toAirportLatitude, toAirportLongitude
        except KeyError:
            raise KeyError("No route exist for given airports")
        
    
def getAirport(fromAirport, toAirport):
    airportsDict = ParseAirports()
    start = None
    end = None
    
    for airport in airportsDict:
        if start is None and airport['airportName'].__contains__(fromAirport):
            start = airport
        elif end is None and airport['airportName'].__contains__(toAirport):
            end = airport
        elif start is not None and end is not None:
            break
    
    return start, end
    
def validateAirportChoice(sourceAirportCode, destAirportCode, airportsList):
    sourceExists = False
    destExists = False
    
    for airport in airportsList:
        if airport.getIATA() == sourceAirportCode:
            sourceExists = True
            # sourceAirport = airport
        elif airport.getIATA() == destAirportCode:
            destExists = True
            # destinationAirport = airport
        if (sourceExists == False or destExists == False):
            return False
        else:
            # return [sourceAirport, destinationAirport]
            return True


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
                
    
# if __name__ == "__main__":
#     main()


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

# def GetUserInput():
#     routesDict = ParseRoutes()
#     airportsDict = ParseAirports()
    
#     routesList = RoutesDictToList(routesDict)
#     airportsList = AirportsDictToList(airportsDict)
    
#     sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
#     destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
    
#     # if airports exists, returns pair of valid Airport objects and assigns to airportExists, else airportExists = None
#     airportsExists = validateAirportChoice(sourceAirportCode, destAirportCode, airportsList)
#     while (airportsExists == None):
#         print("The airport codes you entered were invalid. Please enter again.")
#         sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
#         destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
#         airportsExists = validateAirportChoice(sourceAirportCode, destAirportCode, airportsList)
    
#     # if route exists, returns valid FlightRoute object and assigns to routeExists, else routeExists = None
#     routeExists = validateRoute(sourceAirportCode, destAirportCode, routesList)
#     while (routeExists == None):
#         print("The flight route between your chosen airports does not exist. Please enter again.")
#         # call function to get connecting routes here, using dijkstra algorithm to find shortest path from source to destination 
#         sourceAirportCode = input("Please enter the airport code of the airport you wish to fly from: ")
#         destAirportCode = input("Please enter the airport code of the airport you wish to fly to: ")
#         airportsExists = validateAirportChoice(sourceAirportCode, destAirportCode, airportsList)
#         routeExists = validateRoute(sourceAirportCode, destAirportCode, routesList)
        
#     return airportsExists