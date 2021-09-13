from graph import *

def business_trip(graph: Graph, city_names):
    state=True
    cost=0
    y=city_names[0]
    
    niegh=[city_names[0]]
    for x in city_names:
        if x not in  niegh:
            return [False,0]            
        around=graph.get_neighbours(x)
        niegh=[]
        for n in around:
            niegh.append(n[1])
    around=graph.get_neighbours(y)
    print(around)
    for x in city_names[1:]:
        for n in around:
            if x ==n[1]:
                cost+=n[0]
        around=graph.get_neighbours(x)    
    return [state,cost]
        


        

        


if __name__ == '__main__':

    test = Graph()

    test.add_node('pandora')
    test.add_node('arendelle')
    test.add_node('metroville')
    test.add_node('narina')
    test.add_node('naboo')
    test.add_node('manstropolis')
    test.add_edge('pandora','arendelle',150)
    test.add_edge('pandora','metroville',82)
    test.add_edge('arendelle','pandora',150)
    test.add_edge('arendelle','metroville',99)
    test.add_edge('arendelle','manstropolis',42)
    test.add_edge('metroville','pandora',82)
    test.add_edge('metroville','arendelle',99)
    test.add_edge('metroville','manstropolis',105)
    test.add_edge('metroville','naboo',26)
    test.add_edge('metroville','narina',37)
    test.add_edge('narina','metroville',37)
    test.add_edge('narina','naboo',250)
    test.add_edge('naboo','narina',250)
    test.add_edge('naboo','metroville',26)
    test.add_edge('naboo','manstropolis',73)
    test.add_edge('manstropolis','naboo',73)
    test.add_edge('manstropolis','arendelle',42)
    test.add_edge('manstropolis','metroville',105)
    
   
    print(business_trip(test,['pandora','metroville']))
    print(business_trip(test,['arendelle','manstropolis', 'naboo']))