import unittest
import lca
#comment added to test branching
class TestLCA(unittest.TestCase):

    def test_findLCA(self):

        #test if no tree
        #graph = None
        #root = None
        #self.assertEqual(lca.findLCA(graph, root, "B", "A"), -1)

        # Creating a DAG
        graph = {"G" : []}
        root = "G"
        #test root only tree
        self.assertEqual(lca.findLCA(graph, root, "G", "G"), "G")

        graph = { "A" : [], "B" : ["A"], "C" : ["B"], "D" : ["C"], "E" : ["B"], "F" : ["E"], "G" : ["D", "F"] }


        #test nodes with same parent
        self.assertEqual(lca.findLCA(graph, root, "D", "F"), "G")
        #test nodes with different parent
        self.assertEqual(lca.findLCA(graph, root, "A", "B"), "B")
        #test error scenario: node not in binary tree
        self.assertEqual(lca.findLCA(graph, root, "C", "H"), -1)
        #test error scenario: non string node
        self.assertEqual(lca.findLCA(graph, root, "A", 9), -1)

if __name__ == '__main__':
    unittest.main()
