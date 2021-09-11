from graph import *

#Node can be successfully added to the graph
def test_adding():
    test=Graph()
    test.add_node('e')
    assert test.get_nodes()=={'e'}


#An edge can be successfully added to the graph
def test_get_neighbors():
    test=Graph()
    test.add_node('a')
    test.add_node('b')
    test.add_edge('a','b',3)
    assert test.get_neighbours('a')==[[3, 'b']]

# A collection of all nodes can be properly retrieved from the graph
def test_collections():
    
    teast = Graph()
    teast.add_node('a')
    teast.add_node('b')
    teast.add_node('c')
    teast.add_node('d')
    teast.add_edge('a','b',8)
    teast.add_edge('a','d',2)
    teast.add_edge('a','c')
    teast.add_edge('b','a',4)
    teast.add_edge('c','a',6)
    teast.add_edge('c','d',6)
    teast.add_edge('d','a',5)
    teast.add_edge('d','b',8)
    teast.add_edge('d','c',7)
    assert teast.get_nodes()=={'a','b','c','d'}


# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
def test_neighbors():
    
    teast = Graph()
    teast.add_node('a')
    teast.add_node('b')
    teast.add_node('c')
    teast.add_node('d')
    teast.add_edge('a','b',8)
    teast.add_edge('a','d',2)
    teast.add_edge('a','c')
    teast.add_edge('b','a',4)
    teast.add_edge('c','a',6)
    teast.add_edge('c','d',6)
    teast.add_edge('d','a',5)
    teast.add_edge('d','b',8)
    teast.add_edge('d','c',7)
    assert teast.get_neighbours('a')==[[8, 'b'], [2, 'd'], [1, 'c']]


# The proper size is returned, representing the number of nodes in the graph
def test_size():
    teast = Graph()
    teast.add_node('a')
    teast.add_node('b')
    teast.add_node('c')
    teast.add_node('d')
    teast.add_edge('a','b',8)
    teast.add_edge('a','d',2)
    teast.add_edge('a','c')
    teast.add_edge('b','a',4)
    teast.add_edge('c','a',6)
    teast.add_edge('c','d',6)
    teast.add_edge('d','a',5)
    teast.add_edge('d','b',8)
    teast.add_edge('d','c',7)
    assert teast.size()==4


# A graph with only one node and edge can be properly returned
def test_one_vertex_graph():
    teast = Graph()
    teast.add_node('a')
    assert teast.get_nodes()=={'a'}

#An empty graph properly returns null
def test_empty_graph():
    teast = Graph()
    assert teast.get_nodes()=='Graph is empty'