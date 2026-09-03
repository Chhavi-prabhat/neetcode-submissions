class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            dic[i]=dic.get(i, 0)+1
            length=len(nums)/2
            for key, values in dic.items():
                if values>=length:
                    return key