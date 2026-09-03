class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[]
        for i in range(0, len(arr)):
            num=arr[i]
            if i != len(arr)-1:
                max_num=max(arr[i+1: len(arr)])
                res.append(max_num)
            else:
                res.append(-1)
        return res
        