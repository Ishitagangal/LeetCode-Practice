class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

## WITH DUPLICATES
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1
        if len(nums) == 1:
            if nums[0]!=target:
                return False
            else:
                return True

        while start <= end:
            while start < end and nums[start] == nums[start+1]: # SKIP DUPLICATES
                start += 1
            while start< end and nums[end] == nums[end-1]: # SKIP DUPLICATES
                end -=1
            
            mid = start + (end-start)//2
            if nums[mid] == target:
                return True
            elif nums[start] <= nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False