class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for string in strs:
            string_map = [0] * 26
            for ch in string:
                string_map[ord(ch) - ord('a')] += 1
            string_key = tuple(string_map)

            anagram[string_key].append(string)
        return list(anagram.values())

# Is valid anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dict_s[ord(s[i]) - ord('a')] +=1
        
        for i in range(len(t)):
            dict_s[ord(t[i]) - ord('a')] -=1
            if dict_s[ord(t[i]) - ord('a')] < 0:
                return False
        return True