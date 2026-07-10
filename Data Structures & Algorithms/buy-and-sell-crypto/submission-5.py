class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        left = 0
        for right in range(1,len(prices)):
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            best = max(profit,best)
        return best

            
            

        