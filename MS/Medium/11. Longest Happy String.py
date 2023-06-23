class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # at most 2 continous letters
        # at most a, b, c, occurences of each a, b, c
        #  push num of occurrences and letter into max_heap
        # start with most popular frequency, if 2 same letters added, pop next freq letter, add that, push both back into heap with updated freq
        max_heap = []
        if a!=0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b!=0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c!=0:
            heapq.heappush(max_heap, (-c, 'c'))
        result = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-2] == result[-1] == char:
                if not max_heap:
                    return ''.join(result)
                next_count, next_char = heapq.heappop(max_heap)
                result.append(next_char)
                next_count +=1 # reduce freq in max heap, negative num
                if next_count !=0:
                    heapq.heappush(max_heap, (next_count, next_char))
                heapq.heappush(max_heap, (count, char))
            else:
                result.append(char)
                count += 1
                if count != 0:
                    heapq.heappush(max_heap, (count, char))
        return "".join(result)


## Similar question but just a, b
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        while (a+b > 0):
            if result[-2:] == ['a', 'a']:
                b -=1
                result.append('b')
            elif result[-2:] == ['b', 'b']:
                a -= 1
                result.append('a')
            elif a >= b:
                a -=1
                result.append('a')
            else:
                b-=1
                result.append('b')
        return ''.join(result)