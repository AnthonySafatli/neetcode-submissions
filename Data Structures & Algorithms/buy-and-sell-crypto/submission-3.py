# [10, 1, 2, 4, 3, 10]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        temp_buying = prices[0]
        profit = 0

        for price in prices:
            if  price < temp_buying:
                temp_buying = price
                continue

            temp_profit = price - temp_buying
            if temp_profit > profit:
                profit = temp_profit
                buying = temp_buying

        if profit < 0:
            return 0
        return profit

            
                
            
