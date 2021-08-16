from forimporting import *

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Binary_Tree:
    def __init__(self):
        self.root=None
        self.sol=[]

    def pre_order(self):
        current=self.root
        self.sol=[]
        def pre_order_list(current):
            self.sol.append(current.value)
            if current.left:
                pre_order_list(current.left)
            if current.right:
                pre_order_list(current.right)
        pre_order_list(current)
        return self.sol

    def in_order(self):
        current=self.root
        self.sol=[]
        def in_order_list(current):
            if current.left:
                in_order_list(current.left)
            self.sol.append(current.value)
            if current.right:
                in_order_list(current.right)
        in_order_list(current)
        return self.sol
    def post_order(self):
        current=self.root
        self.sol=[]
        def post_order_list(current):
            if current.left:
                post_order_list(current.left)
            if current.right:
                post_order_list(current.right)
            self.sol.append(current.value)
        post_order_list(current)
        return self.sol
    def tree_max(self):
        temp=self.pre_order()
        sol=0
        for x in temp:
            if x>sol:
                sol=x
        return sol
    
    def breadth_first(self):
        temp=Queue()
        sol=[]
        current=self.root
        temp.enqueue(current)
        while temp.front:
            current=temp.dequeue()
            sol.append(current.value)
            if current.left:
                temp.enqueue(current.left)
            if current.right:
                temp.enqueue(current.right)
           
        return sol



class Binary_Search_Tree(Binary_Tree):
    def add(self,value):
        new_node=Node(value)

        if not self.root:
            self.root=new_node
        else:
            current=self.root
            while True:
                if current.value>value:
                    if not current.left:
                        current.left=new_node
                        break
                    else:
                        current=current.left
                else:
                    if not current.right:
                        current.right=new_node
                        break
                    else:
                        current=current.right

    def contains(self,value):
        values=self.pre_order()
        if value in values:
            return True
        else: 
            return False


if __name__=='__main__':
    bt = Binary_Tree()  
    bt.root = Node(2)    
    bt.root.right = Node(5)    
    bt.root.left = Node(7)    
    bt.root.left.left = Node(2)    
    bt.root.left.right = Node(6)    
    bt.root.right.right = Node(9)    
    bt.root.right.left = Node(4)
    print(bt.pre_order()) 
    print(bt.in_order())
    print(bt.post_order())
    print(bt.breadth_first())
    # test=Binary_Search_Tree()
    # test.add(5)
    # test.add(2)
    # test.add(7)
    # print(test.pre_order())
    # print(test.contains(3))
    # print(bt.tree_max())
    