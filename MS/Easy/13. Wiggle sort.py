class Solution:
    # 2.
    # greedy, O(n)
    def wiggleSortGreedy(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp

        for i in range(len(nums) - 1):
            if i%2 == 0 and nums[i] > nums[i+1]:
                swap(nums, i, i+1)
            elif i%2 == 1 and nums[i] < nums[i+1]:
                swap(nums, i, i +1)

    # 1. sort and then swap every odd index with its next index
    # O(nlogn)
    def wiggleSort(self, nums: List[int]) -> None:
        def swap(nums, a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            swap(nums, i, i+1)
        