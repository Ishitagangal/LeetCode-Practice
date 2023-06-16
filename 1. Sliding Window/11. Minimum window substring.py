# First part: when the right pointer is getting incremented we are decrementing
#  the map count of char if it's part of 't' string. When we see that the map 
#  count of that char after decrementing is positive/zero means that the right 
#  ptr has found a useful char and hence we increment the 'count' variable 
#  (which is keeping track of the number of useful chars)

# Second part: when the left pointer is getting incremented we are essentially 
# making the window smaller and giving back the chars to the map (i.e. 
# incrementing the map count). If we find that for the particular char the map 
# count has now become positive means that we actually gave back a useful char 
# and hence the 'count' is to be decremented.

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, count = 0, 0
        freq = Counter(t)
        ans = ""
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] -= 1
                if freq[s[right]] >= 0:
                    count += 1
            
            while count == len(t):
                if not ans or right - left + 1 < len(ans):
                    ans = s[left : right + 1]
                
                if s[left] in freq:
                    freq[s[left]] += 1
                if freq[s[left]] > 0:
                    count -= 1
                
                left += 1
        
        return ans