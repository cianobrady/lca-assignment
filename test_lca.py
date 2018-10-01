import unittest
import lca

class TestLCA(unittest.TestCase):

    def test_findLCA(self):
        # Creating a binary tree
        node = lca.Node(0)

        node.left = lca.Node(6)
        node.right = lca.Node(2)

        node.left.left = lca.Node(4)
        node.left.right = lca.Node(3)
        node.right.left = lca.Node(1)
        node.right.right = lca.Node(7)

        node.left.right.right = lca.Node(5)
        node.left.right.right = lca.Node(8)
		
        #test nodes with same parent
        self.assertEqual(lca.findLCA(node, 4, 3), 6)
        #test nodes with different parent
        self.assertEqual(lca.findLCA(node, 2, 1), 0)
        #test error scenario: node not in binary tree
        self.assertEqual(lca.findLCA(node, 2, 9), -1)
		
    def test_contains(self):
        # Creating a binary tree
        node = lca.Node(0)

        node.left = lca.Node(6)
        node.right = lca.Node(2)

        node.left.left = lca.Node(4)
        node.left.right = lca.Node(3)
        node.right.left = lca.Node(1)
        node.right.right = lca.Node(7)

        node.left.right.right = lca.Node(5)
        node.left.right.right = lca.Node(8)
        
        #test root
        self.assertEqual(lca.contains(node, 0), True)
        #test key in tree
        self.assertEqual(lca.contains(node, 2), True)
        #test key not in tree
        self.assertEqual(lca.contains(node, 9), False)
