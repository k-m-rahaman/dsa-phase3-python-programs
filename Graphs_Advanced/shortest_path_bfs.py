from collections import deque

def shortest_path(graph, V, src):
    dist = [-1] * V
    dist[src] = 0

    queue = deque([src])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


graph = [[1,2], [3], [3], []]
print(shortest_path(graph, 4, 0))