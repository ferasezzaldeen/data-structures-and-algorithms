from quick import *

def test_one():
    assert 1==1

def test_sort():
    arr=[-1,-2,3,5,4]
    assert Quick_Sort(arr,0,4)==[-2,-1,3,4,5]