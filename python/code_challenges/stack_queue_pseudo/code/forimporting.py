
from typing import Counter


class Node:
  def __init__(self , value=None):
    self.value= value
    self.next=None




class StackEmptyException(Exception):
   pass

class Stack:
    def __init__(self,node=None):
        self.top=node
  
    def push(self, value):
        node= Node(value) 
        node.next = self.top 
        self.top = node

    def pop(self):
        temp=self.top
        self.top=self.top.next
        temp.next=None
        return temp.value

    def peek(self):
        if not self.top:
            raise Exception('empty stack')
        else:
            return self.top.value
    

    def is_empty(self):
        return not self.top    
    
    def __str__(self) -> str:
        str=""
        currunt=self.top
        while currunt:
            str += f"{currunt.value}-> "
            currunt=currunt.next
        str+= "None"
        return str









    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """ create a node containing the value and add it to the rear of our queue"""
        new_node=Node(value)
        if not self.front:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    def dequeue(self):
        if not self.front:
            raise Exception("empty queue")
        else:
            temp=self.front
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            temp.next=None
            
            return temp.value

    def peek(self):
        if not self.front:
            raise Exception("empty queue")
        else:
         
            return self.front.value


    def is_empty(self):
        
        if (not self.rear and self.front) or (self.rear and not self.front):
            raise Exception("empty queue")
        return not self.rear