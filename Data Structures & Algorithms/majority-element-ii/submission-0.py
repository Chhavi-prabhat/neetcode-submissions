class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lim=n//3
        di={}
        out=[]
        for num in nums:
            di[num]=di.get(num,0)+1
        for num,count in di.items():
            if count>lim:
                out.append(num)
        return out     