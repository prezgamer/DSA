from types import NoneType
from Airport import Airport
from DataParser import ParseRoutes, ParseAirports, RoutesDictToList, AirportsDictToList, ParseToAdjList, getCoordinates
from Algorithms import A_star, Dijkstra
from FlightRoute import FlightRoute


def main(fromAirport: str,toAirport: str):
    adjListGraph = ParseToAdjList()
    # need to fill this array with coordinates of all nodes
    coordinates = getCoordinates()
    
    start, end = getAirport(fromAirport, toAirport)
    
    if start is None or end is None:
        print("No such airports exist")
        raise Exception("No such airports exist")
    else:
        try:
            shortest_path, shortest_distance = A_star(adjListGraph.getAdjList(), start['IATA'], end['IATA'], coordinates)
            # shortest_path, shortest_distance = Dijkstra(adjListGraph.getAdjList(), start['IATA'], end['IATA']) 
            shortest_distance = '{:.2f}'.format(shortest_distance)
            
            print(f"The shortest path from {start['airportName']} to {end['airportName']} is: {shortest_path}")
            print(f"The shortest distance from {start['airportName']} to {end['airportName']} is: {shortest_distance} km")
            
            pathNodeCoordinates = []
            
            for node in shortest_path:
                longitude, latitude = coordinates[node]
                pathNodeCoordinates.append((longitude, latitude))

            return shortest_path, pathNodeCoordinates, shortest_distance
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
                
    
if __name__ == "__main__":
    main('Singapore', 'Chinggis')