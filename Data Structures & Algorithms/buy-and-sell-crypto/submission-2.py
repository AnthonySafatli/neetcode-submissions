# [10, 1, 2, 4, 3, 10]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        temp_buying = prices[0]
        profit = 0

        for i in prices:
            if  i < temp_buying:
                temp_buying = i
                continue

            temp_profit = i - temp_buying
            if temp_profit > profit:
                profit = temp_profit
                buying = temp_buying

        if profit < 0:
            return 0
        return profit

            
                
            
