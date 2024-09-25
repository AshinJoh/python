def depthFirst(graph, node):
    stk = [node]

    while stk:
        curr = stk.pop()
        print(curr)

        for item in graph[curr]:
            stk.append(item)

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