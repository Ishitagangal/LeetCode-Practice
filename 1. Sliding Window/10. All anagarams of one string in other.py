class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: # 26 size array
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
        
        p_count =[0] * 26 # O(26) at most
        s_count = [0] * 26 

        for char in p:
            p_count[ord(char) - ord('a')] +=1

        output = []
        # move sliding window of size 3 over the length of s
        for i in range(len_s):
            # add letter to left
            s_count[ord(s[i]) - ord('a')] +=1

            # remove one letter if we have acheived sliding window of 3 by now
            if i >= len_p:
                    s_count[ord(s[i-len_p]) - ord('a')] -=1
            if p_count == s_count:
                output.append(i-len_p + 1) #index of starting point of anagram
        
        return output

    def findAnagramsHashMap(self, s: str, p: str) -> List[int]: # hash table
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
        
        p_count = Counter(p) # O(26) at most
        s_count = Counter() # O(3)

        output = []
        # move sliding window of size 3 over the length of s
        for i in range(len_s):
            # add letter to left
            s_count[s[i]] +=1

            # remove one letter if we have acheived sliding window of 3 by now
            if i >= len_p:
                if s_count[s[i-len_p]] == 1:
                    del s_count[s[i-len_p]]
                else:
                    s_count[s[i-len_p]] -=1
            if p_count == s_count:
                output.append(i-len_p + 1) #index of starting point of anagram
        
        return output