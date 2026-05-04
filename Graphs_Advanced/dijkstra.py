import heapq

def dijkstra(graph, V, src):
    dist = [float('inf')] * V
    dist[src] = 0

    pq = [(0, src)]

    while pq:
        d, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist


graph = [
    [(1,4), (2,1)],
    [(3,1)],
    [(1,2), (3,5)],
    []
]

print(dijkstra(graph, 4, 0))