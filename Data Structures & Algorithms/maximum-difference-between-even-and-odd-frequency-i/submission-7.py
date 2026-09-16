class Solution:
    def maxDifference(self, s: str) -> int:
        hasht={}
        even=float('inf')
        odd=0
        s=s.lower()
        for i in s:
            if i in hasht:
                hasht[i]+=1
            else:
                hasht[i]=1
        for key,value in hasht.items():
            if value%2==0:
                if value<even:
                    even=value
            else:
                if value>odd:
                    odd=value

        return odd-even