class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit_day = 0
        stocks_buy = prices[0]          

        for items in prices:
            if items < stocks_buy:
                stocks_buy = items     
            else:
                profit_day = max(profit_day, items - stocks_buy)   

        return profit_day