from left_joint import *

def test_happy_end():
    hash1 = {
        'fond': 'enamored',
    
    }

    hash2 = {
        'fond': 'averse',
    
    }
    assert left_join(hash1,hash2)==[['fond', 'enamored', 'averse']]


def test_right_is_empty():
    hash1 = {
        'fond': 'enamored',
      
    }

    hash2 = {
        
    }
    assert left_join(hash1,hash2)==[['fond', 'enamored', None]]

def test_left_is_empty():
    hash1 = {
     
    
    }

    hash2 = {
        'fond': 'averse',
    
    }
    assert left_join(hash1,hash2)==[]