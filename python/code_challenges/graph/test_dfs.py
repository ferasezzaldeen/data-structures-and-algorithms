from graph import *


def test_dfs():
    teast = Graph()
    teast.add_node('a')
    teast.add_node('b')
    teast.add_node('c')
    teast.add_node('d')
    teast.add_node('x')
    teast.add_edge('a','b')
    teast.add_edge('a','c')
    teast.add_edge('b','d')
    teast.add_edge('b','x',)
    
    
    assert teast.depth_first('a')==['a', 'b', 'd', 'x', 'c']