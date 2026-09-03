class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for i in range(0, len(s)):
            if s[i] in "({[":
                stack.append(s[i])
                top+=1
            elif s[i] in ")}]":
                if top==-1:
                    return False
                if (s[i]==")" and stack[top]!="(") or (s[i]=="]" and stack[top]!="[") or(s[i]=="}" and stack[top]!="{"):
                    return False
                stack.pop()
                top-=1
     
        return top==-1