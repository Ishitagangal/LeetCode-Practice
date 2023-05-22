class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: # more optimized, keep num matched char
        counter = Counter(s1)
        match = 0
        len_s1 = len(s1)

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -=1
                if counter[s2[i]] == 0: match +=1
            if i>=len_s1 and s2[i-len_s1] in counter:
                if counter[s2[i-len_s1]] == 0: #moving window over, if the letter was a match reduce match of chars due to moving sliding window
                    match -=1
                counter[s2[i-len_s1]] +=1
            if match == len(counter):
                return True
        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        counter, s1_len = Counter(s1), len(s1)
        window_start = 0
        for window_end in range(len(s2)):
            if s2[window_end] in counter:
                counter[s2[window_end]] -= 1
            if window_end >= s1_len and s2[window_end - s1_len] in counter:
                counter[s2[window_end-s1_len]] += 1
                
            
            if all([counter[i]==0 for i in counter]):
                return True
        return False

    