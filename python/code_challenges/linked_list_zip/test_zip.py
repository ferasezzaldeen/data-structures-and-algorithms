from forimporting import *
from linked_list_zip import *


#test if the function work 
def test_zip_list():
    first=LinkedList()
    second=LinkedList()
    first.appendvalue(11)
    first.appendvalue(12)
    first.appendvalue(13)
    first.appendvalue(14)
    second.appendvalue(21)
    second.appendvalue(22)
    second.appendvalue(23)
    second.appendvalue(24)
    new=zip_lists(first,second)
    actual=new.__str__()
    expected='11 -> 21 -> 12 -> 22 -> 13 -> 23 -> 14 -> 24 -> NULL'
    assert actual==expected

#test if the function work when the first list is longer from the second
def test_zip_list_first_is_longer():
    first=LinkedList()
    second=LinkedList()
    first.appendvalue(11)
    first.appendvalue(12)
    first.appendvalue(13)
    first.appendvalue(14)
    second.appendvalue(21)
    second.appendvalue(22)

    new=zip_lists(first,second)
    actual=new.__str__()
    expected='11 -> 21 -> 12 -> 22 -> 13 -> 14 -> NULL'
    assert actual==expected

#test if the function work when the second list is longer from the first
def test_zip_list_second_is_longer():
    first=LinkedList()
    second=LinkedList()
    first.appendvalue(11)
    first.appendvalue(12)
    second.appendvalue(21)
    second.appendvalue(22)
    second.appendvalue(23)
    second.appendvalue(24)
    new=zip_lists(first,second)
    actual=new.__str__()
    expected='11 -> 21 -> 12 -> 22 -> 23 -> 24 -> NULL'
    assert actual==expected
