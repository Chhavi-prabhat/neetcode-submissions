class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(0, len(prices)):
            mini=prices[i]
            for j in range(i+1, len(prices)):
                if prices[j]> prices[i]:
                    profit=prices[j]-mini
                    if profit>max_profit:
                        max_profit=profit
        return max_profit
        