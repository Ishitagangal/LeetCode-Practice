def countRotations(arr, n):
    pivot = findPivot(arr, n)
    return pivot + 1 # find pivot element, [7, 8, 9, 1, 2, 3, 4, 5], pivot = 2, rotations = 3

def findPivot(arr, n):
    low = 0
    high = n - 1
 
    while low <= high:
        mid = low + (high - low) // 2
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if mid > low and arr[mid - 1] > arr[mid]:
            return mid - 1
        if arr[low] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1