import unittest
import lca

class TestLCA(unittest.TestCase):

    def test_findLCA(self):

        #test if no graph
        graph = None
        root = None
        self.assertEqual(lca.findLCA(graph, root, "B", "A"), -1)

        # Creating a DAG
        graph = {'G' : []}
        root = 'G'
        #test root only graph
        self.assertEqual(lca.findLCA(graph, root, 'G', 'G'), 'G')

        graph = { 'A' : [], 'B' : ['A'], 'C' : ['B'], 'D' : ['C'], 'E' : ['B'], 'F' : ['E'], 'G' : ['D', 'F'] }


        #test nodes with same parent
        self.assertEqual(lca.findLCA(graph, root, 'D', 'F'), 'G')
        #test nodes with different parent
        self.assertEqual(lca.findLCA(graph, root, 'A', 'B'), 'B')
        #test error scenario: node not in graph
        self.assertEqual(lca.findLCA(graph, root, 'C', 'H'), -1)
        #test error scenario: non string node
        self.assertEqual(lca.findLCA(graph, root, 'A', 9), -1)


    def test_shortest_path(self):
        #test empty graph
        graph = None
        self.assertEqual(lca.shortest_path(graph, "B", "A"), [])

        #test one node graph
        graph = {'A' : []}
        self.assertEqual(lca.shortest_path(graph, 'A', 'A'), ['A'])

        #test graph
        graph = { 'A' : [], 'B' : ['A'], 'C' : ['B'], 'D' : ['C'], 'E' : ['B'], 'F' : ['H'], 'G' : ['D', 'F'], 'H' : ['E'] }
        self.assertEqual(lca.shortest_path(graph, 'G', "A"), ['G', 'D', 'C', 'B', 'A'])

        #test error scenario: element not in graph
        self.assertEqual(lca.shortest_path(graph, 'Z', 'A'), [])

        #test error scenario: wrong type
        self.assertEqual(lca.shortest_path(graph, 'A', 9), [])

if __name__ == '__main__':
    unittest.main()
