# Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
# Output: 3
# Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
# - Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
# - Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
# - Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # calculate sum of each
        # reduce array with bigger sum and icnrease array with smaller sum
        # at each step in sorted order, change the num in the array that has the 
        # greatest distance from 6 to minimize total num of operations needed
        # instead of a heap can also sort and iterate in opp. dir
        sum1, sum2 = sum(nums1), sum(nums2)
        # swap for the rest of the logic
        if sum1 > sum2:
            sum1, sum2 = sum2, sum1 # so sum1 < sum2 for rest of the logic
            nums1, nums2 = nums2, nums1
        heapq.heapify(nums1) #min heap
        nums2 = [-num for num in nums2] # max heap
        heapq.heapify(nums2)
        result = 0
        diff = sum2 - sum1
        while diff > 0 and nums1 and nums2:
            a = 6 - nums1[0]
            b = (-nums2[0]) - 1
            if a > b:
                heapq.heappop(nums1)
                diff -= a
            else:
                heapq.heappop(nums2)
                diff -= b
            result +=1
        while diff>0 and nums1:
            diff -= (6 - heapq.heappop(nums1))
            result += 1
        while diff > 0 and nums2:
            diff -= (-heapq.heappop(nums2) - 1)
            result += 1
        return result if diff <= 0 else -1

        