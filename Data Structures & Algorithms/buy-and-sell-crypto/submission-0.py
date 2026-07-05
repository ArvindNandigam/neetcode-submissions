class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        lb = prices[0]
        for i in range(1,len(prices)):
            lb = min(prices[i],lb)
            mp = max(prices[i]-lb,mp)
        return mp