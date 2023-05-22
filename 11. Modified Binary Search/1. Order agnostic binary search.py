def binarySearch(arr, start, end, x):
 
    is_ascending = arr[start] < arr[end]
     
    while (start <= end):
        middle = start + (end - start) // 2
 
        if (arr[middle] == x):
            return middle
 
        if (is_ascending == True):
             if (arr[middle] < x):
                start = middle + 1
             else:
                end = middle - 1
 
        else:
            if (arr[middle] > x):
                start = middle + 1
            else:
                end = middle - 1
 
    return -1