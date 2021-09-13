from bf import *

def test_happy():
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
    
   
    assert business_trip(test,['pandora','metroville'])==[True, 82]

def test_failed():
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
    
   
    assert business_trip(test,['pandora','naboo'])==[False,0]
