# Graphs
<!-- Short summary or background information -->
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge
<!-- Description of the challenge -->
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

* add node
* add edge
* get nodes
* get neighbors
* size

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O: Time: O(n^2) Space: O(n)

the code is shown here [code](./graph.py)

the tests are shown here [test](./test_graph.py)
## API
<!-- Description of each method publicly available in your Graph -->
add node: will make a new node
add edge: will make a new edge between 2 nodes
get nodes: will return all the nodes inside a graph
git neighbors: will return all the nodes connected to a specific node
size: will return the numbers of nodes in the graph
