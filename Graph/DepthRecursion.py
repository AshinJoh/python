def depthFirst(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end = " ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            depthFirst(graph, neighbour, visited)

# Adjancey List Representation
graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : [],
}

depthFirst(graph, 'a')