from trees import *



#Can successfully instantiate an empty tree
def test_empty_tree():
    test=Binary_Tree()
    assert test.root==None


#Can successfully instantiate a tree with a single root node
def test_single_root_node():
    test=Binary_Tree()
    test.root = Node(2)  
    assert test.root.value==2
#Can successfully add a left child and right child to a single root node
def test_left_and_right_children_nodes():
    test=Binary_Tree()
    test.root = Node(2)
    test.root.right = Node(5)    
    test.root.left = Node(7)      
    assert test.root.left.value==7 and test.root.right.value==5
#Can successfully return a collection from a preorder traversal
def test_preorder():
    test=Binary_Tree()
    test.root = Node(2)
    test.root.right = Node(5)    
    test.root.left = Node(7) 
    assert test.pre_order()==[2,7,5]
#Can successfully return a collection from an inorder traversal
def test_inorder():
    test=Binary_Tree()
    test.root = Node(2)
    test.root.right = Node(5)    
    test.root.left = Node(7) 
    assert test.in_order()==[7,2,5]
#Can successfully return a collection from a postorder traversal
def test_postorder():
    test=Binary_Tree()
    test.root = Node(2)
    test.root.right = Node(5)    
    test.root.left = Node(7) 
    assert test.post_order()==[7,5,2]
