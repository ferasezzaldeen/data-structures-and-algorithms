from forimporting import *

open_brackets=['(','[','{']
close_brackets=[')',']','}']


def validate_brackets(string):
    store=Stack()
    for x in string:
        if x in open_brackets:
            store.push(x)
        elif x in close_brackets:
            index=close_brackets.index(x)
            if not store.is_empty() and open_brackets[index]==store.peek():
                store.pop()
            else:
                return False
    if store.top==None:
        return True
    else:
        return False




if __name__=="__main__":
    print(validate_brackets('{kiki()}'))

