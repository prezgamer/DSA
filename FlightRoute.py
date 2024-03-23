class FlightRoute:
    airline = ""
    sourceAirport = ""
    destinationAirport = ""
    distance = 0.0

    def __init__(self, airline, sourceAirport, destinationAirport, distance):
        self.airline = airline
        self.sourceAirport = sourceAirport
        self.destinationAirport = destinationAirport
        self.distance = distance

    def getSource(self):
        return self.sourceAirport
    
    def getDestination(self):
        return self.destinationAirport
    
    def getDistance(self):
        return self.distance