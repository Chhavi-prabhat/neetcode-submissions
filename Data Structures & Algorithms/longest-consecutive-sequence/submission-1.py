class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_count=1
        count=1
        s=sorted(set(nums))
        for i in range(1,len(s)):
            if s[i]==s[i-1]+1:
                count+=1
                max_count=max(count,max_count)
            else:
                count=1
        return max_count      