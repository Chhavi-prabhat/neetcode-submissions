import math
def totaltimecal(piles: List[int],k: int) -> int:
    time=0
    for i in piles:
        time+=math.ceil(i/k)
    return time

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)+1
        ans=max(piles)
        while low<=high:
            mid=(low+high)//2
            timetook=totaltimecal(piles,mid)
            if timetook <=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
