import heapq
from math import radians, cos, sin, asin, sqrt

"""
Calculate the great circle distance in kilometers between two points 
on the earth (specified in decimal degrees)
"""
def Haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

"""
Calculates the shortest path from start airport to end airport, and returns the route.
Using an adjacency list of flight routes
"""
def Dijkstra(adjacency_list, start, end):
    # Initialize distances from start to all other nodes as infinity
    distances = {node: float('inf') for node in adjacency_list}
    distances[start] = 0  # Distance from start to start is 0

    # Initialize priority queue with start node
    pq = [(0, start)]  # Priority queue (distance, node)
    predecessors = {}  # Keep track of predecessors

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if we have already found a shorter path to this node
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in adjacency_list[current_node]:
            distance = current_distance + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node  # Update predecessor
                heapq.heappush(pq, (distance, neighbor))

    # Backtrack to construct the shortest path
    shortest_path = []
    current_node = end
    while current_node != start:
        shortest_path.append(current_node)
        current_node = predecessors[current_node]
    shortest_path.append(start)
    shortest_path.reverse()  # Reverse the path to get start to end order

    return shortest_path


# Example adjacency list of flight routes
# adjacency_list = {
#     'A': [('B', 10), ('C', 3)],
#     'B': [('C', 1), ('D', 2)],
#     'C': [('B', 4), ('D', 8), ('E', 2)],
#     'D': [('E', 7)],
#     'E': [('D', 9)]
# }

# start = 'A'
# end = 'E'

# shortest_path, shortest_distance = Dijkstra(adjacency_list, start, end)
# print(f"The shortest path from {start} to {end} is: {shortest_path}")
# print(f"The shortest distance from {start} to {end} is: {shortest_distance}")


