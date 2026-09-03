class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        for i in range(0, len(nums)):
            count=0
            if nums[i]==1:
                for j in range(i, len(nums)):
                    if nums[j]==1:
                        count+=1
                        max_count=max(count, max_count)
                    else:
                        break
        return max_count