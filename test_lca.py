import unittest
import lca

class TestLCA(unittest.TestCase):

    def test_findLCA(self):
        # Creating a binary tree
        node = Node(0)

        node.left = Node(6)
        node.right = Node(2)

        node.left.left = Node(4)
        node.left.right = Node(3)
        node.right.left = Node(1)
        node.right.right = Node(7)

        node.left.right.right = Node(5)
        node.left.right.right = Node(8)
		
		#test nodes with same parent
        self.assertEqual(lca.findPath(node, 4, 3), 6)
		
		#test nodes with different parent
		self.assertEqual(lca.findPath(node, 2, 1), 0)
		
		#test error scenario: node not in binary tree
		self.assertEqual(lca.findPath(node, 2, 9), -1)
		
