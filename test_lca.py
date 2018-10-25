import unittest
import lca
#comment added to test branching
class TestLCA(unittest.TestCase):

    def test_findLCA(self):

        #test if no tree
        graph = None
        self.assertEqual(lca.findLCA(graph, "B", "A"), -1)

        # Creating a DAG
        graph = {"A" : []}
        #test root only tree
        self.assertEqual(lca.findLCA(graph, "A", "A"), "A")

        graph = { "A" : [], "B" : ["A"], "C" : ["B"], "D" : ["C"], "E" : ["B"], "F" : ["E"], "G" : ["D", "F"] }


        #test nodes with same parent
        self.assertEqual(lca.findLCA(graph, "D", "F"), "G")
        #test nodes with different parent
        self.assertEqual(lca.findLCA(graph, "A", "B"), "B")
        #test error scenario: node not in binary tree
        self.assertEqual(lca.findLCA(graph, "C", "H"), -1)
        #test error scenario: non string node
        self.assertEqual(lca.findLCA(graph, "A", 9), -1)
