def has_cycle_dfs(graph, V):
    visited = [False] * V
    recStack = [False] * V

    def dfs(node):
        visited[node] = True
        recStack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recStack[neighbor]:
                return True

        recStack[node] = False
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i):
                return True
    return False


# Example
graph = [[1], [2], [0]]
print(has_cycle_dfs(graph, 3))