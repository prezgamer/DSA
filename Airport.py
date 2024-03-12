class Airport:
    airportName = ""
    city = ""
    country = ""
    IATA = ""
    latitude = 0.0
    longitude = 0.0
    
    def __init__(self, airportName, city, country, IATA, latitude, longitude):
        self.airportName = airportName
        self.city = city
        self.country = country
        self.IATA = IATA
        self.latitude = latitude
        self.longitude = longitude

    def getIATA(self):
        return self.IATA
    
    def getLatitude(self):
        return self.latitude
    
    def getLongitude(self):
        return self.longitude