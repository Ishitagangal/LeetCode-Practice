class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr # to avoi dempty stack
        result = [0] * len(arr)
        stack = [0]
        for i in range(len(arr)):
            while stack and arr[i]< arr[stack[-1]]:
                stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i-j) * arr[i]
            stack.append(i)
        return sum(result) %(10**9+7)


# Sum of subarray ranges
# Let's ask a different question - what is the sum of the minimum element of all subarrays? 
# This is exactly this problem: 907. Sum of Subarray Minimums. 
# With this method, we can also find the sum of the maximum element of all subarrays.

# The solution for this problem can be formulated as sum(max(b)) - sum(min(b)),
#  where b ranges over every (contiguous) subarray of n.
# call same function and find sum of subarray maximums - sumof subarray minimums
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        arr = [0] + nums # to avoi dempty stack
        def sum_subarray_min_or_max(operation):
            result = [0] * len(arr)
            stack = [0]
            for i in range(len(arr)):
                while stack and operation(arr[i],arr[stack[-1]]): 
                    stack.pop()
                j = stack[-1] if stack else 0 # stack wouldbe empty for greater than 
                result[i] = result[j] + (i-j) * arr[i]
                stack.append(i)
            return sum(result)
        return sum_subarray_min_or_max(gt) - sum_subarray_min_or_max(lt)