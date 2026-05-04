from collections import deque

def topo_sort_kahn(graph, V):
    indegree = [0] * V

    for u in range(V):
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([i for i in range(V) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result


graph = [[1,2], [3], [3], []]
print(topo_sort_kahn(graph, 4))