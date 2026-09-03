class Solution:
    def scoreOfString(self, s: str) -> int:
        result=0
        for ch in range(len(s)-1):
            result+=abs(ord(s[ch+1])-ord(s[ch]))
        return result