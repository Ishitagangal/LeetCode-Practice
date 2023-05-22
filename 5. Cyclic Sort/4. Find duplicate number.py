class Solution:
    def findDuplicate2(self, nums: List[int]) -> int: # binary search
        low = 1
        high = len(nums) - 1

        while low <= high:
            cur = (low + high) //2
            count = 0

            count = sum(num <= cur for num in nums)
            if count > cur: # duplicate num in left side of midpoint found
                dup = cur
                high = cur - 1
            else:
                low = cur + 1
        return dup
    
    def findDuplicate(self, nums:List[int]) -> int: # cycle detection O(n)
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast