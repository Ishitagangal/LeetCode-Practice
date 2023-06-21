class Solution:
    # https://medium.com/hackernoon/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029
    def knightDialer(self, n: int) -> int:
        neighbors = {
        0:(4,6),
        1:(6,8),
        2:(7,9),
        3:(4,8),
        4:(0,3,9),
        5:(),
        6:(0,1,7),
        7:(2,6),
        8:(1,3),
        9:(2,4)
        }
        prior_hop = [1] * 10
        current_hop = [0] * 10
        for i in range(n-1):
            current_hop = [0] * 10
            for num in range(10):
                for neighbor in neighbors[num]:
                    current_hop[neighbor] = (current_hop[neighbor] + prior_hop[num]) % (10**9 + 7)
            prior_hop = current_hop
        return sum(prior_hop) % (10**9 + 7)

# Recursive with memoization, O(n)
# def count_sequences(start_position, num_hops):
#     cache = {}

#     def helper(position, num_hops):
#         if (position, num_hops) in cache:
#             return cache[ (position, num_hops) ]

#         if num_hops == 0:
#             return 1

#         else:
#             num_sequences = 0
#             for neighbor in neighbors(position):
#                 num_sequences += helper(neighbor, num_hops - 1)
#             cache[ (position, num_hops) ] = num_sequences
#             return num_sequences

#     res = helper(start_position, num_hops)
#     return res