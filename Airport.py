class Airport:
    airportID = 0
    airportName = ""
    city = ""
    country = ""
    IATA = ""
    ICAO = ""
    latitude = 0.0
    longitude = 0.0
    
    def __init__(self, airportID , airportName, city, country, IATA, ICAO, latitude, longitude):
        self.airportID = airportID
        self.airportName = airportName
        self.city = city
        self.country = country
        self.IATA = IATA
        self.ICAO = ICAO
        self.latitude = latitude
        self.longitude = longitude

    def getIATA(self):
        return self.IATA
    
    def getName(self):
        return self.airportName
    
    def getLatitude(self):
        return self.latitude
    
    def getLongitude(self):
        return self.longitude