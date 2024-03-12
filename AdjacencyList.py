class Graph:

    adjList = {}

    def __init__(self, routesList):
        for route in routesList:
            self.addEdge(route[0], route[1])
            

    def addEdge(self, v, w):
        if v in self.adjList:
            self.adjList[v].append(w)
        else:
            self.adjList[v] = []
            self.adjList[v].append(w)

        if w in self.adjList:
            self.adjList[w].append(v)
        else:
            self.adjList[w] = []
            self.adjList[w].append(v)

    
    def getAdjList(self, v):
        return self.adjList[v]
    
    
    def printAdjList(self, airportCode):
        print("Adjacent airports to " + airportCode + "are:")
        for adjAirport in self.getAdjList(airportCode):
            print(adjAirport)