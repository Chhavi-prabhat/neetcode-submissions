class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if sorted(nums)==nums:
            return True
        elif sorted(nums, reverse=True)==nums:
            return True
        else:
            return False
        