from forimporting import *

class Pseudo_Queue(Stack):
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,value):
        self.stack1.push(value)
        return self.stack1

    def dequeue(self):
        currunt=self.stack1.top
        counter=0
        while currunt:
            self.stack2.push(currunt.value)
            currunt=currunt.next
            counter+=1
        for x in range(counter):
            self.stack1.pop()
        sol=self.stack2.pop()
        currunt= self.stack2.top
        while currunt:
            self.stack1.push(currunt.value)
            currunt=currunt.next
        return sol



if __name__ =='__main__':
    print("hello")
    test=Pseudo_Queue()
    test.enqueue(5)
    test.enqueue(4)
    test.enqueue(3)
    print(test.enqueue(2))
    print(test.dequeue())



