from forimporting import LinkedList,Node




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
    sec=new.__str__
    print(sec)
    


    
    




