from trees import *

def tree_intersection(first: Binary_Tree,second: Binary_Tree):
    
    if(first.root and second.root):
        list1=first.pre_order()
        list2=second.pre_order()
        sol=[]
        for x in list1:
            for i in list2:
                if x==i:
                    sol.append(x)
        if sol:
            return sol
        else:
            return 'there is no intersection'
    else:
        return 'there is an empty tree'
    
    
if __name__ == '__main__':
    test1 = Binary_Tree()
    test1.root = Node(90)
    test1.root.right = Node(80)
    test1.root.left = Node(100)

    test2 = Binary_Tree()
    test2.root = Node(20)
    test2.root.right = Node(10)
    test2.root.left = Node(100)
 
 

    print(tree_intersection(test1,test2))