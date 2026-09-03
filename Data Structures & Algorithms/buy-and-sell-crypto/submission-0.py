class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        coll=[]
        for i in range(0, len(prices)):
            mini=prices[i]
            for j in range(i+1, len(prices)):
                if prices[j]> prices[i]:
                    profit=prices[j]-mini
                    coll.append(profit)
        if coll:
            return max(coll)
        else: 
            return 0
        