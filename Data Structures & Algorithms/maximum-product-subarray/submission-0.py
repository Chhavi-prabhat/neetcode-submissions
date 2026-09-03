class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pr=[]
        n=len(nums)
        for i in range(0, n):
            prod=1
            for j in range(i,n):
                prod*=nums[j]
                pr.append(prod)
        return max(pr)
