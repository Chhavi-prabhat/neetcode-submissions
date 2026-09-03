class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        t_list=list(t)
        for i in s:
            if i in t_list:
                t_list.remove(i)
            else:
                return False
        return True    