class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - buying_price
            if profit > max_profit:
                max_profit = profit
            if buying_price > prices[i]:
                buying_price = prices[i]
        return max_profit