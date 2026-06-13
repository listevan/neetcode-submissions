class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ma = 0
        mi = prices[0]

        for price in prices:
            ma = max(ma, price-mi)
            mi = min(mi, price)
        
        return ma
        