graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

def bfs(graph, initial):
    visited = []
    queue = [initial]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            for neighbour in graph[node]:
                queue.append(neighbour)

    return visited

print(graph)
print(bfs(graph, 'A'))