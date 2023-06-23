class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # find minimum number i nthe array
        # subtract every other num with this one to find number of steps to make it equal
        # [5,6,7,8] can be made equal if we decrement number 8, three times and 7, two times 
        # and 6 one times. Decrementing 8 by 1 is equal to adding 1 to all the other elements.
        min_num = min(nums)
        result = 0
        for num in nums:
            result += num - min_num
        return result