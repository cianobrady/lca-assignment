class Graph:
    # Graph constructor
    def __init__(self):
        self.edges = {}
        self.vertices = {}
        self.vertices_count = 0
        self.edges_count = 0

    def addVertex(self, key):
        vertex = Vertex(key)
        self.vertices[vertices_count] = vertex
        self.vertices_count = vertices_count + 1

    def addEdge(self, src, dst):
        edge = Edge(src, dst)
        self.edges[edges_count] = edge
        self.edges_count = edges_count + 1

class Vertex:
    # Vertex constructor
    def __init__(self, key):
        self.key = key

class Edge:
    # Edge constructor
    def __init__(self, src, dst):
        srcVertex = Vertex(src)
        srcVertex = Vertex(dst)
        self.src = srcVertex
        self.dst = dstVertex

#findLCA takes in the root of a tree and two nodes and returns the LCA of the two nodes if they are both present in the tree\
def findLCA(root, key1, key2):
    #if tree does not contain key, return error
    if( not (contains(root, key1) and contains(root, key2))):
        return -1

    path1 = []
    path2 = []
    #creating paths from root to given keys
    path1 = path(root, key1)
    path2 = path(root, key2)

    #verifies when paths differ and determines that the node in each path before the difference is the LCA
    i=0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

#path takes in a root of a tree and a key within that tree and returns the path from the root to that key
def path(root, key):
    if not root:
        return []
    if root.key == key:
        return[root.key]
    temp = path(root.left, key)
    if temp:
        return [root.key] + temp
    temp = path(root.right, key)
    if temp:
        return [root.key] + temp
    return []

#contains function takes in root of tree and a key and returns whether the tree contains the key
def contains(root, key):
    if not root:
        return False
    if root.key == key:
        return True
    return contains(root.left, key) or contains(root.right, key)
