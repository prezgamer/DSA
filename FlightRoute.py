from numpy import source


class FlightRoute:
    airline = ""
    sourceAirport = ""
    destinationAirport = ""

    def __init__(self, airline, sourceAirport, destinationAirport):
        self.airline = airline
        self.sourceAirport = sourceAirport
        self.destinationAirport = destinationAirport

    def getSource(self):
        return self.sourceAirport
    
    def getDestination(self):
        return self.destinationAirport