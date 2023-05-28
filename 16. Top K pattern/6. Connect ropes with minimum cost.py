#connect ropes with minimum cost
# minimum when we add smallest ropes first

def min_cost(ropes, n):
    heapq.heapify(ropes)

    result = 0

    while len(ropes) > 1:
        first_rope = heapq.heappop(ropes)
        second_rope = heapq.heappop(ropes)

        result += first_rope + second_rope
        heapq.heappush(ropes, first_rope+second_rope)

    return result