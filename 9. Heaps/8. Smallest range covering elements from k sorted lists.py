class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # min heap of smallest nums, init right to max of the 0th elements
        # as you pop from heap see if left, right can be made smaller

        min_heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(min_heap)
        result = -inf, inf
        right = max(row[0] for row in nums)
        while min_heap:
            left, i, j = heapq.heappop(min_heap)
            if right - left < result[1] - result[0]:
                result = (left, right)
            if j + 1 == len(nums[i]):
                break
            new_max_candidate = nums[i][j+1]
            right = max(right, new_max_candidate)
            heapq.heappush(min_heap, (new_max_candidate, i, j+1))
        return result