class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        # below also works for looping instead of modulo for index i.
        # for i in list(range(len(nums))) * 2 :
        for i in range(len(nums) * 2): #loop twice since circular, if it wasn't circular loop once
            i = i % (len(nums))
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i] # nums[i] is next greater element for stack top
            stack.append(i)
        
        return result
        
# Next smaller element
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices

# Discount ith item by the next smallest element's value and return array