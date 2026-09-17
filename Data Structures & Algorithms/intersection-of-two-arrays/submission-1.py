class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op=[]
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        for i in nums1:
            if i in nums2 and i not in op:
                op.append(i)
        return op
        