#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def max_profit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit_value = 0

        for price in prices[1:]:
            max_profit_value = max(max_profit_value, price - min_price)
            min_price = min(min_price, price)

        return max_profit_value