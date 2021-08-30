def marge(left,right,arr):
    i=0
    j=0
    k=0
    while (i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1

    if i == len(left):
        while j<len(right):
            arr[k]=right[j]
            k+=1 
            j+=1
    else:
         while i<len(left):
            arr[k]=left[i]
            k+=1 
            i+=1
    return arr

def Mergesort(arr):
    n= len(arr)
    if n>1:
        mid=n//2
        # print (mid)
        left=arr[0:mid]
        right=arr[mid:n]
        Mergesort(left)
        Mergesort(right)
        marge(left,right,arr)
        return arr

if __name__=='__main__':
    print(Mergesort([8,-5,4,16,15,42,23,55]))

