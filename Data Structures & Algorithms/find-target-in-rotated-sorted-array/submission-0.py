class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums=sorted(nums)
        count=0
        for i in nums:
            if target!=i:
                count+=1
            else:
                return count
        if target not in nums:
            return -1
        return count