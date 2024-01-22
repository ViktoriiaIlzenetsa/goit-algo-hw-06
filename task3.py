from task1 import graph_creating

def print_table(distances, visited):
    # Верхній рядок таблиці
    print("|{:<10}|{:<10}|{:<10}|".format("Вершина", "Ціна", "Перевірено"))
    print("|"+"-" * 10+"|"+"-"*10+"|"+"-"*10+"|")
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("|{:<10}|{:<10}|{:<10}|".format(vertex, distance, status))
    print("\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
    # Вивід таблиці 
    print_table(distances, visited)

    return distances

if __name__ == "__main__":
    G = graph_creating()
    graph = {}
    for i in G.nodes:
        graph[i] = {}
        for key, value in G[i].items():
            graph[i][key] = value["weight"]


    for key in graph.keys():
        dijkstra(graph, key)