from collections import deque

def has_cycle_kahn(graph, V):
    indegree = [0] * V

    for u in range(V):
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([i for i in range(V) if indegree[i] == 0])
    count = 0

    while queue:
        node = queue.popleft()
        count += 1

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return count != V


# Example
graph = [[1], [2], [0]]
print(has_cycle_kahn(graph, 3))