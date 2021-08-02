import pytest
from linked_list import __version__


def test_version():
    assert __version__ == '0.1.0'






#import the "Subject Under Test"
from  linked_list.linked_lists import LinkedList, Node






# Can successfully instantiate an empty linked list
def test_linkedlist():
    assert LinkedList()


# Can properly insert into the linked list
def test_insert():
  # arrange
    ll = LinkedList()
    with pytest.raises(AttributeError):
        ll.head.value
    ll.insert(5)
    actual = ll.head.value
    assert actual == 5

#The head property will properly point to the first node in the linked list
def test_if_head_is_head():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert(45)

    current=test.head
    current=current.next
    while current:
        if current.next==test.head:
            assert False
        else:
            current=current.next
    return False





#Can properly insert multiple nodes into the linked list
def test_inserting_more():
    expected="45 -> 55 -> 66 -> NULL"
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    actual=test.__str__()
    assert actual==expected

# Will return true when finding a value within the linked list that exists
def test_true_includes():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    actual=test.includes(55)
    assert actual==True

#Will return false when searching for a value in the linked list that does not exist
def test_false_includes():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    actual=test.includes(555)
    assert actual==False


# Can properly return a collection of all the values that exist in the linked list
def test_all_values_property():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    if ((66 in test.values) and(55 in test.values) and(45 in test.values)):
        assert True
    else:
        assert False

# Can successfully add a node to the end of the linked list
def test_append():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.appendvalue(77)
    expected="45 -> 55 -> 66 -> 77 -> NULL"
    actual=test.__str__()
    assert actual==expected

# Can successfully add multiple nodes to the end of a linked list
def test_multi_append():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.appendvalue(77)
    test.appendvalue(88)
    expected="45 -> 55 -> 66 -> 77 -> 88 -> NULL"
    actual=test.__str__()
    assert actual==expected

# Can successfully insert a node before a node located i the middle of a linked list
def test_insert_befor():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert_befor(55,50)
    expected="45 -> 50 -> 55 -> 66 -> NULL"
    actual=test.__str__()
    assert actual==expected

#Can successfully insert a node before the first node of a linked list

def test_first_insert():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert_befor(45,50)
    expected="50 -> 45 -> 55 -> 66 -> NULL"
    actual=test.__str__()
    assert actual==expected

#Can successfully insert after a node in the middle of the linked list
def test_insert_after():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert_after(55,50)
    expected="45 -> 55 -> 50 -> 66 -> NULL"
    actual=test.__str__()
    assert actual==expected


#Can successfully insert a node after the last node of the linked list
def test_insert_after_last():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert_after(66,50)
    expected="45 -> 55 -> 66 -> 50 -> NULL"
    actual=test.__str__()
    assert actual==expected


# Where k is greater than the length of the linked list

def test_kth_from_end():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert(35)
    test.insert(30)
    test.insert(25)
    test.insert(20)
    test.insert(15)
    test.insert(10)
    
    expected=35
    actual=test.kth_from_end(3)
    assert actual==expected


#Where k and the length of the list are the same
def test_kth_same_length():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert(35)
    expected='the k value is the same as the length of the list, please change it'
    actual=test.kth_from_end(4)
    assert actual==expected

# Where k is not a positive integer
def test_kth_is_negative():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert(35)
    expected='k is negative, please enter a positive number'
    actual=test.kth_from_end(-1)
    assert actual==expected

# Where the linked list is of a size 1
def test_kth_when_list_length_equal_one():
    test=LinkedList()
    test.insert(66)
    expected=66
    actual=test.kth_from_end(0)
    assert actual==expected

#“Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_kth_where_k_is_in_the_middle():
    test=LinkedList()
    test.insert(66)
    test.insert(60)
    test.insert(55)
    test.insert(45)
    test.insert(35)
    expected=55
    actual=test.kth_from_end(2)
    assert actual==expected
