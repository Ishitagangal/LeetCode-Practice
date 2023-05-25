class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = left + (right - left) // 2
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element 
            # the least value is on right
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value smallest value is to the left
            else:
                right = mid - 1