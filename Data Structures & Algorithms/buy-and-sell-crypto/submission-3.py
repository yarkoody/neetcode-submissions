class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,1
        maxP = 0
        curr = 0

        while sell < (len(prices)):
            # if not profitable replace the pointer of buy with sell since its lower

            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy + 1
            else:
                curr = prices[sell] - prices[buy]
                maxP = max(maxP, curr) 
                sell += 1
        return maxP
        