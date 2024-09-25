def BreadthFirst(graph, node):
    visited = set()
    queue = [node]
    while queue:
        curr = queue.pop(0)

        if curr not in visited:
            print(curr, end=' ')
            visited.add(curr)

        for neigbours in graph[curr]:
            if neigbours not in visited:
                queue.append(neigbours)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}


BreadthFirst(graph, 'A')