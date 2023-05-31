class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    
    # O(n)
    # If we had some way of counting instances of the majority element as +1+1+1
# and instances of any other element as −1-1−1, summing them would make it
# obvious that the majority element is indeed the majority element.
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate