from types import NoneType
from Airport import Airport
from DataParser import ParseRoutes, ParseAirports, RoutesDictToList, AirportsDictToList, ParseToAdjList, getCoordinates
from Algorithms import A_star, Dijkstra
from FlightRoute import FlightRoute


def main(fromAirport: str,toAirport: str, airportsBST, adjListGraph, cost):
    
    # get start and end airport objects
    start, end = getAirport(fromAirport, toAirport, airportsBST)
    
    if start is None or end is None:
        print("No such airports exist")
        raise Exception("No such airports exist")
    else:
        try:
            shortest_path, shortest_distance = A_star(adjListGraph.getAdjList(), start, end, airportsBST)
            shortest_distance = '{:.2f}'.format(shortest_distance)
            cost = shortest_distance * 1.2
            pathNodeCoordinates = []
            
            for node in shortest_path:
                airport = airportsBST.get(node)
                longitude = airport.getLongitude()
                latitude = airport.getLatitude()
                pathNodeCoordinates.append((longitude, latitude))

            for i in range(0, len(shortest_path)):
                shortest_path[i] = airportsBST.get(shortest_path[i]).getName()
                
            return shortest_path, pathNodeCoordinates, shortest_distance, cost
        except KeyError:
            raise KeyError("No route exist for given airports")
        
    
def getAirport(fromAirport, toAirport, airportsBST):
    airportsDict = ParseAirports()
    start = None
    end = None
    
    for airport in airportsDict:
        if start is None and airport['airportName'].casefold().__contains__(fromAirport.casefold()):
            start = airport['IATA']
            start = airportsBST.get(start)
        elif end is None and airport['airportName'].casefold().__contains__(toAirport.casefold()):
            end = airport['IATA']
            end = airportsBST.get(end)
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
#     main('singapore', 'narita')