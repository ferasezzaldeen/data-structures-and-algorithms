from trees import *

def fizz_buzz_tree(tree):
    node=tree.root
    temp=[]
    def fizzbuzz(node):
        if node.value%3==0 and node.value%5==0:
            temp.append('FizzBuzz')
        elif node.value%3==0:
            temp.append('Fizz')
        elif node.value%5==0:
            temp.append('Buzz')
        else:
            temp.append(node.value)
        
        if node.left:
            fizzbuzz(node.left)
        if node.right:
            fizzbuzz(node.right)
    fizzbuzz(node)
    sol=Binary_Search_Tree()
    for x in temp:
        sol.add(x)
    return sol




if __name__=='__main__':
    bt = Binary_Tree()  
    bt.root = Node(15)    
    bt.root.right = Node(5)    
    bt.root.left = Node(3)    
    bt.root.left.left = Node(5)    
    bt.root.left.right = Node(5)    
    bt.root.right.right = Node(3)    
    bt.root.right.left = Node(3)
    test=fizz_buzz_tree(bt)
    print(test.pre_order())