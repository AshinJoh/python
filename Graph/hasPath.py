def hasPath(graph, src, dest):
    if src == dest:
        return True
    
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dest) == True:
            return True

    return False
graph = {
    'f' : ['g', 'i'],
    'g' : ['h'],
    'h' : [],
    'i' : ['g','k'],
    'j' : ['i'],
    'k' : []
}

print(hasPath(graph, 'f', 'k'))