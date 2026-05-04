def topo_sort_dfs(graph, V):
    visited = [False] * V
    stack = []

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    for i in range(V):
        if not visited[i]:
            dfs(i)

    return stack[::-1]


graph = [[1,2], [3], [3], []]
print(topo_sort_dfs(graph, 4))