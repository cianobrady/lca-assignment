
#findLCA takes in the root of a tree and two nodes and returns the LCA of the two nodes if they are both present in the tree\
def findLCA(graph, root, key1, key2):
    #if tree does not contain key, return error
    if not graph or not root:
        return -1
    if(key1 not in graph ) or (key2 not in graph):
        return -1

    #creating paths from root to given keys
    nodes = []
    for node in graph:
        nodes.append(node)

    #creates a list containing the depth of each node
    depths = []
    i = 0
    while(i<len(nodes)):
        shortest = shortest_path(graph, root, nodes[i])
        if not shortest:
            depths.append(None)
        else:
            depths.append(len(shortest)-1)
        i = i+1

    i = 0
    lca = None
    max_depth = 0
    while(i<len(nodes)):
        test1 = shortest_path(graph, nodes[i], key1)
        test2 = shortest_path(graph, nodes[i], key2)
        if (test1!=None) and (test2!=None) and (depths[i]!=None):
            if(depths[i]>=max_depth):
                max_depth = depths[i]
                lca = nodes[i]
        i = i+1
    return lca

#paths takes in a graph and two keys within that graph and returns the path from the first key to the second key
#paths was developed using graph tutorial at https://www.python.org/doc/essays/graphs/
def shortest_path(graph, key1, key2, path=[]):
    path = path + [key1]
    if key1 == key2:
        return path
    if key1 not in graph:
        return []
    shortest = None
    for newKey in graph[key1]:
        if newKey not in path:
            new = shortest_path(graph, newKey, key2, path)
            if new:
                if not shortest or len(new) < len(shortest):
                    shortest = new
    return shortest
