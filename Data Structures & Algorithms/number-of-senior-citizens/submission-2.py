class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages=[]
        count=0
        for d in details:
            ages.append(d[11:13])
        for i in ages:
            if int(i)>60:
                count+=1
        return count