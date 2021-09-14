from forimporting import *

class Vertex:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_node(self ,value):
        node = Vertex(value)
        self.adjacency[node] = []
        return node

    def add_edge(self, first_vertex, second_vertex, weight=1):
        check = False
        for i in self.adjacency.keys():
            if str(i.value) == str(first_vertex):
                
                check = True
                break
            else:
                
                check = False
        
        for i in self.adjacency.keys():
            if str(i.value) == str(second_vertex):
                
                check = True
                break
            else:
                check = False
       
        if check:
            for i in self.adjacency.keys():
                if str(i.value) == str(first_vertex):
                
                    self.adjacency[i].append([weight,second_vertex])
                    break
                else:
                
                    continue
            
        else:
            return 'one of the vertex is not exist'


    def bfs(self, start_node):
        nodes=set([])
        temp = [start_node]
        values = []

        while len(temp) >0:
            front_node = temp.pop(0)
            nodes.add(front_node)

            for i in self.adjacency.keys():
                if str(i.value) == str(front_node):
                    values.append(self.adjacency[i])
                    break

            if len(values) > 0:
                for n in values[0]:
                    if n[1] not in nodes:
                        temp.append(n[1])
                        nodes.add(n[1])
            else:
                return False
        return nodes


    def depth_first(self,node:Vertex):
        sol=[]
        def inside(node:Vertex):
            sol.append(node)
            nigh=self.get_neighbours(node)
            for x in nigh:
                inside(x[1])
        inside(node)    
        return sol


    def get_nodes(self):
        if len(list(self.adjacency.keys())) > 0:
            start = list(self.adjacency.keys())[0].value
            return self.bfs(start)
        else:
            return 'Graph is empty'

    def get_neighbours(self, node):
        if len(list(self.adjacency.keys())) > 0:

            for i in self.adjacency.keys():
                if str(i.value) == node:
                    return self.adjacency[i]
            
            return 'Node does not exist'
        else:
            return 'Graph is empty'

    def size(self):
        if len(list(self.adjacency.keys())) > 0:
            start = list(self.adjacency.keys())[0].value
            return len(self.bfs(start))
        else:
            return 'Graph is empty'

if __name__=='__main__':
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
    
    print(teast.get_nodes())
    print(teast.get_neighbours('a'))
    print(teast.bfs('a'))
    teast.depth_first('a')