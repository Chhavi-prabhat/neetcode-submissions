class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        triple=sorted([nums[i], nums[j], nums[k]])
                        if triple not in res:
                            res.append(triple)
        return res