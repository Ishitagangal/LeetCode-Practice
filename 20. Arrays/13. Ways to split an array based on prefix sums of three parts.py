# The array is split into three non-empty contiguous subarrays - 
# named left, mid, right respectively from left to right.
# The sum of the elements in left is less than or equal to the sum
#  of the elements in mid, and the sum of the elements 
# in mid is less than or equal to the sum of the elements in right.
# Input: nums = [1,2,2,2,5,0]
# Output: 3
# Explanation: There are three good ways of splitting nums:
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
class Solution:
    # calculate prefix sums
    # prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
    # 2 * prefix[i] <= prefix[left_boundary] or j
    # 2 * prefix[right_boundary] <= prefix[-1] + prefix[i] or k
    # result ++ (k -j) such that maximum k and minimum j
    # sum(0, i) <= sum(i + 1, j), and sum(i + 1, k - 1) < sum(k, n).
    def waysToSplit(self, nums:List[int]) -> int: # Linear O(n)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        result = 0
        lower = upper = 0
        for i in range(1, len(nums)): # 0th index is 0 in prefix
            lower = max(lower, i+1)
            while lower < len(nums) and prefix[lower] < 2* prefix[i]:
                lower +=1
            upper = max(upper, lower)
            while upper<len(nums) and 2 * prefix[upper] <= (prefix[-1] + prefix[i]):
                upper +=1
            result += upper - lower
        return result % (10**9+7)

    def waysToSplit2(self, nums: List[int]) -> int: # Binary search (O nlogn)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        result = 0
        for i in range(1, len(prefix)-2): # -2 because we are looking for 2 indices, j and k
            # j
            lower = self.binarySearch(prefix, prefix[i] * 2, True)
            # k
            upper = self.binarySearch(prefix, (prefix[-1] + prefix[i])/2, False)
            result += max(0, min(upper, len(prefix)-1) - max(lower, i+1))
        return result % (10**9+7)
    
    def binarySearch(self, arr, target, lower=True): # lowerbound or upper bound
        left, right = 0, len(arr)
        while left<right:
            mid = left + (right-left)//2
            if lower:
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            else:
                if arr[mid] <= target:
                    left = mid+1
                else:
                    right = mid
        return right
