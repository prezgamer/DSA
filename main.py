from DataParser import ParseAirports
from Algorithms import A_star
from FlightRoute import FlightRoute
from bst import bst

def main(fromAirport: str,toAirport: str, airportsBST, adjListGraph):
    
    # get start and end airport objects
    start, end = getAirport(fromAirport, toAirport, airportsBST)
    
    if start is None or end is None:
        print("No such airports exist")
        raise Exception("No such airports exist")
    else:
        try:
            shortest_path, shortest_distance = A_star(adjListGraph.getAdjList(), start, end, airportsBST)
            shortest_distance = '{:.2f}'.format(shortest_distance)
            cost = '{:.2f}'.format(float(shortest_distance) * 0.2)
            pathNodeCoordinates = []
            
            for node in shortest_path:
                airport = airportsBST.get(node)
                longitude = airport.getLongitude()
                latitude = airport.getLatitude()
                pathNodeCoordinates.append((longitude, latitude))

            for i in range(0, len(shortest_path)):
                shortest_path[i] = "{country} ({IATA}), {name}".format(country = airportsBST.get(shortest_path[i]).getCountry(), IATA = airportsBST.get(shortest_path[i]).getIATA(), name = airportsBST.get(shortest_path[i]).getName())
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