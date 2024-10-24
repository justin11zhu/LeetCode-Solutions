#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lowest = prices[0]
        for n in prices:
            if n < lowest:
                lowest = n
            if result < n - lowest:
                result = n - lowest
        return result