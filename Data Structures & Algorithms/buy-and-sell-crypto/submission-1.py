class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,1
        maxProfit = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy += 1
                sell = buy + 1
            else:
                curr = prices[sell] - prices[buy]
                maxProfit = max(maxProfit,curr)
                sell += 1
        return maxProfit



