# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
class Solution:
    # put freq of each char in max heap
    # if top two frequent ones are equal, -1 for one of them and push it back in
    # if top two have diff freq then top of heap is unique and pop it out
    # continue until only one char left in heap
    def minDeletions(self, s: str) -> int:
        char_freq = [0] * 26
        for char in s:
            char_freq[ord(char) - ord('a')] +=1
        
        max_heap = [-freq for freq in char_freq if freq!=0]
        heapq.heapify(max_heap)

        min_deletion = 0
        while len(max_heap) > 1:
            top_char_freq = -heapq.heappop(max_heap)
            if top_char_freq == -max_heap[0]:
                # if equal, decrement top char and push back in
                if top_char_freq -1 > 0:
                    top_char_freq -=1
                    heapq.heappush(max_heap, -top_char_freq)
                min_deletion +=1
        return min_deletion