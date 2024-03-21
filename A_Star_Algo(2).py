import heapq
from math import radians, cos, sin, asin, sqrt

def Haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
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
        # Pop from heap to get smallest (distance, node) pair in priority queue
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

    return shortest_path, distances[end]


# calculate the shortest path from start to end using A* algorithm with the given adjacency list and coordinates 
def A_star(adjacency_list, start, end, coordinates):
    # Initialize distances from start to all other nodes as infinity
    distances = {node: float('infinity') for node in adjacency_list}
    distances[start] = 0 # Distance from start to start is 0

    # Initialize priority queue with start node
    priority_queue = [(Haversine(coordinates[start][1], coordinates[start][0], coordinates[end][1], coordinates[end][0]), 0, start)]
    predecessors = {} # Keep track of predecessors

    while priority_queue:
        # pop from heap to get smallest (estimated_total_cost, current_distance, current_node) pair in priority queue
        estimated_total_cost, current_distance, current_node = heapq.heappop(priority_queue)

        # skip if we have already found a shorter path to this node
        if current_node == end:
            break

        # explore neighbors of the current node
        for neighbour, weight in adjacency_list[current_node]:
            distance = current_distance + weight

            # update distance once a shorter path is found
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                neighbour_coordinate = coordinates[neighbour]
                end_coordinate = coordinates[end]
                estimated_cost_to_end = Haversine(neighbour_coordinate[1], neighbour_coordinate[0], end_coordinate[1], end_coordinate[0])
                total_estimated_cost = distance + estimated_cost_to_end 
                heapq.heappush(priority_queue, (total_estimated_cost, distance, neighbour))
                predecessors[neighbour] = current_node
    
    # backtrack to construct the shortest path
    shortest_path = []
    current_node = end
    while current_node != start:
        shortest_path.append(current_node)
        current_node = predecessors.get(current_node, start) # If no predecessor, then we have reached the start
    shortest_path.append(start)
    shortest_path.reverse()  # Reverse the path to get start to end order
    
    # Return the shortet path and the distance from the start to the end
    return shortest_path, distances[end]

# Example coordinates for each node (airport)
coordinates = {
    'A': (34.5, -123.4),  
    'B': (35.4, -124.5), 
    'C': (36.3, -125.6),  
    'D': (37.2, -126.7),
    'E': (38.1, -127.8),
}

# Example adjacency list of flight routes
adjacency_list = {
    'A': [('B', 10), ('C', 3)],
    'B': [('C', 1), ('D', 2)],
    'C': [('B', 4), ('D', 8), ('E', 2)],
    'D': [('E', 7)],
    'E': [('D', 9)],
}

start = 'A'
end = 'E'

# Call the A_star function with the example data
shortest_path, shortest_distance = A_star(adjacency_list, start, end, coordinates)
print(f"The shortest path from {start} to {end} is: {shortest_path}")
print(f"The shortest distance from {start} to {end} is: {shortest_distance} km")