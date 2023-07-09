class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        updates = [0 for _ in range(len(s))]
        for start, end, dir in shifts:
            if dir == 0: 
                updates[start] -= 1
                if end < len(s)-1:
                    updates[end+1] +=1
            else:
                updates[start] +=1
                if end < len(s) - 1:
                    updates[end+1] -= 1
        sum = 0
        for i in range(len(s)):
            sum += updates[i] # sum will indicate how much to shift by 
            new_letter = chr((ord(s[i]) - ord('a') + sum) % 26 + 97)
            s = s[:i] + new_letter + s[i+1:]
        return s