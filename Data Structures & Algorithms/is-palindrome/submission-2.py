class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls=[]
        revls=[]
        for i in s:
            if i==" " or i in "?,.$%^&*!~`/\|+-_=@':;":
                continue
            ls.append(i.lower())
        for a in s[::-1]:
            if a==" " or a in "?,.$%^&*!~`/\|+-_=@':;":
                continue
            revls.append(a.lower())
        if revls==ls:
            return True
        else:
            return False
        