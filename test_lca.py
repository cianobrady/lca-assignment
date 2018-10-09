import unittest
import lca
#comment added to test branching
class TestLCA(unittest.TestCase):

    def test_findLCA(self):

        #test if no tree
        node = None
        self.assertEqual(lca.findLCA(node, 4, 3), -1)

        # Creating a binary tree
        node = lca.Node(0)

        #test root only tree
        self.assertEqual(lca.findLCA(node, 0, 0), 0)

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
        self.assertEqual(lca.findLCA(node, 2, 1), 2)
        #test error scenario: node not in binary tree
        self.assertEqual(lca.findLCA(node, 2, 9), -1)
        #test error scenario: non integer node
        self.assertEqual(lca.findLCA(node, "a", 9), -1)

    def test_contains(self):
        #test if no tree
        node = None
        self.assertEqual(lca.contains(node, 0), False)

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

    def test_path(self):
        #test if no tree
        node = None
        self.assertEqual(lca.path(node, 0), [])

        # Creating a binary tree
        node = lca.Node(0)

        node.left = lca.Node(6)
        node.right = lca.Node(2)

        node.left.left = lca.Node(4)
        node.left.right = lca.Node(3)
        node.right.left = lca.Node(1)
        node.right.right = lca.Node(7)

        node.left.right.right = lca.Node(5)
        node.left.right.right.left = lca.Node(8)

        #test root
        self.assertEqual(lca.path(node, 0), [0])
        #test key in tree
        self.assertEqual(lca.path(node, 2), [0, 2])
        self.assertEqual(lca.path(node, 8), [0, 6, 3, 5, 8])
        #test key not in tree
        self.assertEqual(lca.path(node, 9), [])
