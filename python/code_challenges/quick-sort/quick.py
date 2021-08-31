def swap(arr,i,low):
    temp=arr[i]
    arr[i]=arr[low]
    arr[low]=temp

def partition(arr,left,right):
    pivot=arr[right]
    low=left-1
    for i in range(left,right):
        if arr[i]<=pivot:
            low+=1
            swap(arr,i,low)
    swap(arr,right,low+1)  
    return low+1

def Quick_Sort(arr,left,right):
    if left<right:
        position=partition(arr,left,right)

        Quick_Sort(arr,left,position-1)
        Quick_Sort(arr,position+1,right)
    return arr


if __name__=='__main__':
    print(Quick_Sort([55,77,88,5,1,63,2],0,6))

