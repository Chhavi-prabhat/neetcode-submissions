class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op=[]
        nums1=list(set(sorted(nums1)))
        nums2=list(set(sorted(nums2)))
        for i in nums1:
            if i in nums2:
                op.append(i)
        return op
        