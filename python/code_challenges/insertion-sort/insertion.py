
def sort(arr):
    
    for i in range(len(arr)):
        current = i 
        next = i+1
        if i == len(arr)-1:
            break
        for trial in range(len(arr)-1):  
            if arr[next] < arr[current]:
                current = next
            next +=1
            if next > len(arr)-1:
                break
        temp = arr[current]
        arr[current] = arr[i]
        arr[i] = temp       
    return arr
   
        

if __name__ == "__main__":
    print(sort([6,85,454,22,13,-9,56,77,-77]))
   
 
