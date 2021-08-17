from tree_fizz_buzz import *

def test_fizz_buzz():
    bt = Binary_Tree()  
    bt.root = Node(15)    
    bt.root.right = Node(5)    
    bt.root.left = Node(3)    
    bt.root.left.left = Node(5)    
    bt.root.left.right = Node(5)    
    bt.root.right.right = Node(3)    
    bt.root.right.left = Node(3)
    test=fizz_buzz_tree(bt)
    assert test.pre_order()==['FizzBuzz', 'Fizz', 'Buzz', 'Buzz', 'Buzz', 'Fizz', 'Fizz'] 