class Graph:

    adjList = {}

    def __init__(self, routesList):
        for route in routesList:
            self.addEdge(route.getSource(), route.getDestination(), route)
            
    
    def addEdge(self, v, w, route):
        if v in self.adjList:
            self.adjList[v].append([w, route.getDistance()])
        else:
            self.adjList[v] = []
            self.adjList[v].append([w,route.getDistance()])

        if w in self.adjList:
            self.adjList[w].append([v,route.getDistance()])
        else:
            self.adjList[w] = []
            self.adjList[w].append([v,route.getDistance()])

    
    def getAdjList(self):
        return self.adjList