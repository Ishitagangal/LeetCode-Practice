# find an element in an array of infinite size
 
def binary_search(arr,low,high,x):
 
    if high >= low:
        mid = low + (high - low)//2
 
        if arr[mid] == x:
            return mid
 
        if arr[mid] > x:
            return binary_search(arr,low,mid-1,x)
 
        return binary_search(arr,mid+1,high,x)
 
    return -1
# assume a is infinite and we cant use len(a) to find its size
def findPos(arr, key):
 
    low, high, val = 0, 1, arr[0]
 
    while val < key:
        low = high          #store previous high
        high = 2*high          #double high index
        val = arr[high]       #update new val
 
    return binary_search(arr, low, high, key)