class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters) - 1

        while (low<=high):
            mid = low + (high-low)//2

            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        
        if low == len(letters):
            return letters[0]
        else:
            return letters[low]