import unittest
import lca
#comment added to test branching
class TestLCA(unittest.TestCase):

    def test_findLCA(self):

        #test if no tree
        graph = None
        self.assertEqual(lca.findLCA(graph, 4, 3), -1)

        # Creating a DAG
        graph = lca.Graph()

        #test root only tree
        graph.addVertex(0)
        self.assertEqual(lca.findLCA(graph, 0, 0), 0)

        graph.addVertex(0)
        graph.addVertex(1)
        graph.addVertex(2)
        graph.addVertex(3)
        graph.addVertex(4)
        graph.addVertex(5)
        graph.addVertex(6)

        graph.addEdge(6, 3)
        graph.addEdge(6, 5)
        graph.addEdge(3, 2)
        graph.addEdge(5, 4)
        graph.addEdge(2, 1)
        graph.addEdge(4, 1)
        graph.addEdge(1, 0)


        #test nodes with same parent
        self.assertEqual(lca.findLCA(graph, 2, 4), 6)
        #test nodes with different parent
        self.assertEqual(lca.findLCA(graph, 0, 1), 1)
        #test error scenario: node not in binary tree
        self.assertEqual(lca.findLCA(graph, 2, 9), -1)
        #test error scenario: non integer node
        self.assertEqual(lca.findLCA(graph, "a", 9), -1)
