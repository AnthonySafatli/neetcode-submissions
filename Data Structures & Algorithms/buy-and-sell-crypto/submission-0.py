# [10, 1, 2, 4, 3, 10]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buying = prices[0]
        temp_buying = buying
        profit = prices[1] - buying

        for i in range(1, len(prices)):
            if prices[i] < buying and prices[i] < temp_buying:
                temp_buying = prices[i]
                continue

            temp_profit = prices[i] - temp_buying
            if temp_profit > profit:
                profit = temp_profit
                buying = temp_buying

        if profit < 0:
            return 0
        return profit

            
                
            
