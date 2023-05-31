class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_zeroes = 0
        for i in range(0, len(arr)):
            if arr[i]==0:num_zeroes +=1
        
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + num_zeroes <n:
                arr[i+ num_zeroes] = arr[i]
            if arr[i] == 0:
                num_zeroes -=1
                if i+num_zeroes<n:
                    arr[i + num_zeroes] = 0
        