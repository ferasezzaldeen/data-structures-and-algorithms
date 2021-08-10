from forimporting import *

class Dog():
    def __init__(self,name):
        self.name = name
        self.type = 'dog'
        self.next = None

class Cat():
    def __init__(self,name):
        self.name = name
        self.type = 'cat'
        self.next = None
    
   



class AnimalShelter :
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self,animal):
        if animal.type == 'cat':
            self.cat.enqueue(animal.name)
            print('Add Cat')

        elif animal.type == 'dog':
            self.dog.enqueue(animal.name)
            print('Add Dog')
    def dequeue(self, pref):

        if pref == "dog":
            self.dog.dequeue()

        elif pref == "cat":
            self.cat.dequeue()
        else:
            return 'Null'
    






 

