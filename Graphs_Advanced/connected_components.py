def connected_components(graph, V):
    visited = [False] * V
    components = []

    def dfs(node, comp):
        visited[node] = True
        comp.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, comp)

    for i in range(V):
        if not visited[i]:
            comp = []
            dfs(i, comp)
            components.append(comp)

    return components


graph = [[1], [0], [3], [2]]
print(connected_components(graph, 4))