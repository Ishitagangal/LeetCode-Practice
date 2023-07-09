class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def binarySearch(house):
            left = 0
            right = len(heaters) -1
            while left<=right:
                mid = (right + left) // 2
                if heaters[mid] < house:
                    left = mid + 1
                elif heaters[mid] >= house:
                    right = mid - 1
                
            return left

        heaters.sort()
        result = 0
        # i = 0
        for house in houses:
            # while house > heaters[i+1]: # or binary search to find where it falls
            #     i +=1 
            i = binarySearch(house)
            if i == len(heaters):
                result = max(result, house - heaters[-1])
            elif i == 0:
                result = max(result, heaters[0] - house)
            else:
                result = max(result, min(house - heaters[i-1], heaters[i] - house))
            # result = max(result, distance)
        return result