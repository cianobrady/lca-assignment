
#findLCA takes in the root of a tree and two nodes and returns the LCA of the two nodes if they are both present in the tree\
def findLCA(graph, root, key1, key2):
    #if tree does not contain key, return error
    if(key1 not in graph ) or (key2 not in graph):
        return -1

    path1 = []
    path2 = []
    #creating paths from root to given keys
    path1 = paths(graph, root, key1)
    path2 = paths(graph, root, key2)

    #verifies when paths differ and determines that the node in each path before the difference is the LCA
    i=0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

#paths takes in a graph and two keys within that graph and returns the path from the first key to the second key
#paths was developed using graph tutorial at https://www.python.org/doc/essays/graphs/
def paths(graph, key1, key2, path=[]):
    path = path + [key1]
    if key1 == key2:
        return path
    for newKey in graph[key1]:
        if newKey not in path:
            thePath = paths(graph, newKey, key2, path)
            if thePath:
                return thePath
    return None
