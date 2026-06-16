class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumprice = float('inf')
        maximumprofit = 0 
        for price in prices:
            if price < minimumprice:
                minimumprice = price
            elif price - minimumprice > maximumprofit:
                maximumprofit = price - minimumprice
        return maximumprofit 
