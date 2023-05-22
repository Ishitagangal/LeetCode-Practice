# in sorted array find the element that has the minimum difference with target
# find floor and ceil of target and take the min. difference of the two

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low<=high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return arr[mid] # diff would 0 with itself obv
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    # floor is arr[high], ceil is arr[low]
    if target - arr[high] < arr[low] -  target:
        return arr[high]
    return arr[low]
