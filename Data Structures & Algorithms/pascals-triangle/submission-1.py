class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        for i in range(numRows-1):
            temparr=[0] + res[-1] + [0]
            new=[]
            for j in range(len(res[-1])+1):
                new.append(temparr[j]+ temparr[j+1])
            res.append(new)
        return res