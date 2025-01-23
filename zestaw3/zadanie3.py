import heapq

def dijkstra(graph, start):
    

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))


    distances = {node: float('inf') for node in graph}
    distances[start] = 0


    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)


        if current_distance > distances[current_node]:
            continue


        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight


            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

# Example
if __name__ == "__main__":
    # Example graph as an adjacency list
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 6},
        'C': {'A': 4, 'B': 2, 'D': 3},
        'D': {'B': 6, 'C': 3}
    }

    start_node = 'A'
    distances, previous_nodes = dijkstra(graph, start_node)

    print("Shortest distances from node A:")
    for node, distance in distances.items():
        print(f"Node {node}: {distance}")

    print("\nPrevious nodes in the shortest path tree:")
    for node, prev in previous_nodes.items():
        print(f"Node {node}: {prev}")
