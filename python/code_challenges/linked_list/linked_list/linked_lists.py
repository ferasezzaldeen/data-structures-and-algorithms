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



if __name__ == "__main__":
  ll = LinkedList()
  ll.insert(5)
  ll.insert(4)
  print(ll)
  node1 =  Node(1)
  node2 =  Node(2)
  node3 = node1 + node2
  print(node3)

  for value in ll:
    print(value)
