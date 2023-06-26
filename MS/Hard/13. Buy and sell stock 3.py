class Solution:
    # At most 2 transactions can be made, and they can not be overlapping
    # find left profit up to i, find righ profits from i to n
    # add them to find max possible at that split stage of i
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        left_profits = [0] * length
        # pad the right DP array with an additional zero for convenience.
        right_profits = [0] * (length + 1)

        # construct the bidirectional DP array
        for i in range(1, length):
            left_profits[i] = max(left_profits[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])

            r = length - 1 - i
            right_profits[r] = max(right_profits[r+1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

        return max_profit
        
        