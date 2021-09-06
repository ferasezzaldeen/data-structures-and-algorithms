from intersection import *


def test_intersection():
    test1 = Binary_Tree()
    test1.root = Node(90)
    test1.root.right = Node(80)
    test1.root.left = Node(100)

    test2 = Binary_Tree()
    test2.root = Node(20)
    test2.root.right = Node(10)
    test2.root.left = Node(100)
    assert tree_intersection(test1,test2)==[100]

def test_intersection_failuer():
    test1 = Binary_Tree()
    test1.root = Node(90)
    test1.root.right = Node(80)
    test1.root.left = Node(100)

    test2 = Binary_Tree()
   
    assert tree_intersection(test1,test2)=='there is an empty tree'

def test_no_intersection():
    test1 = Binary_Tree()
    test1.root = Node(90)
    test1.root.right = Node(80)
    test1.root.left = Node(100)

    test2 = Binary_Tree()
    test2.root = Node(20)
    test2.root.right = Node(10)
    test2.root.left = Node(101)
    assert tree_intersection(test1,test2)=='there is no intersection'