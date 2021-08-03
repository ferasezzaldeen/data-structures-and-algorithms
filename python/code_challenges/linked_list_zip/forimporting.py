class Node:
    def __init__(self, value=""):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None
        self.values=[]

    def insert(self, value):
        self.values.append(value)
        node = Node(value)

        if self.head:
            node.next = self.head

        self.head = node


    def includes(self,value):
        current=self.head
        while current:
            if current.value==value:
                return True
            else:
                current=current.next
        return False


    def __str__(self):
        string = ""
        current = self.head

        while current:
            string += f"{str(current.value)} -> "
            current = current.next
        string += "NULL"
        return string

    def appendvalue(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
        else:
            currunt=self.head
            while currunt.next:
                currunt=currunt.next
            currunt.next=new_node
        
       
                
    def insert_befor(self,value,new_value):
        new_node=Node(new_value)
        if self.head.value==value:
            self.insert(new_value)
        else:
            currunt=self.head
            while currunt.next:
                if currunt.next.value==value:
                    new_node.next=currunt.next
                    currunt.next=new_node
                    break
                currunt=currunt.next

    def insert_after(self,value,new_value):
        new_node=Node(new_value)
        if self.head.value==value:
            self.head.next=new_node
        else:
            currunt=self.head
            while currunt:
                if currunt.value==value:
                    new_node.next=currunt.next
                    currunt.next=new_node
                    break
                currunt=currunt.next   

    def kth_from_end(self,num):
        current=self.head
        sol=[]
        if num<0:
            return 'k is negative, please enter a positive number'
        
        counter=0
        while current.next:
            counter +=1
            current=current.next
        if counter+1==num:
            return 'the k value is the same as the length of the list, please change it'
        if counter<num:
            raise Exception
        position=counter-num
        current=self.head
        for x in range(position):
            current=current.next
        return current.value
    
        # while current:
        #     sol.append(current.value)
        #     current=current.next
        # if len(sol)> num:
        #     sol.reverse()
        #     return sol[num]
        # elif len(sol)==num:
        #     return 'the k value is the same as the length of the list, please change it'
        # elif len(sol)<num:

        #     raise Exception

        


def zip_lists(first:LinkedList,second:LinkedList):
    var1 =first.head
    var2=second.head
    
    new=LinkedList()
    while True:
        if var1:
            new.appendvalue(var1.value)
            var1=var1.next
        
        if var2:
            new.appendvalue(var2.value)
            var2=var2.next
        
        if not var1 and not var2 :
            break

    return new



if __name__ == "__main__":
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
    print(new)
