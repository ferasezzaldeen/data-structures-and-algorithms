from hash import *


#Adding a key/value to your hashtable results in the value being in the data structure

def test_add():
    test=HashTable()
    test.add('ahmad',555)
    assert test.contains('ahmad')==True



# Retrieving based on a key returns the value stored
def test_get():
    test=HashTable()
    test.add('ahmad',555)
    assert test.get('ahmad')==555

#Successfully returns null for a key that does not exist in the hashtable
def test_null_get():
    test=HashTable()
    
    assert test.get('ahmmad')==None

#Successfully handle a collision within the hashtable
def test_collision():
    test=HashTable()
    test.add('feras',555)
    test.add('saref',666)
    assert test.get('feras')==555


#Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_collision_retrieve():
    test=HashTable()
    test.add('feras',555)
    test.add('saref',666)
    assert (test.get('feras')==555 and test.get('saref')==666 )