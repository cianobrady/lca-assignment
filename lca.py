class Node:
    # Node constructor
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
		
def findLCA(root, node1, node2):
    
    if( not (contains(root, node1) and contains(root, node2))):
        return -1
    
    path1 = []
    path2 = []
    
    path1 = path(root, node1, path1)
    path2 = path(root, node2, path2)
    
    i=0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]
    
    
def path(root, key, p):
    if root == None:
        return []
    if root.key == key:
        p.append(root.key)
        return p
    
    
    if( path(root.left, key, p) or path(root.left, key, p)):
        p.append(root.key)
    print(p)
    return p
        
	 
def contains(root, key):
    #sample code to test python unit testing
	if(key >= 0 and key <=8):
		return True
	return False
	
