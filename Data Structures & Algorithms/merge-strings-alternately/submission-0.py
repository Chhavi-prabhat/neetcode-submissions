class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        op=[]
        w1=len(word1)
        w2=len(word2)
        for a,b in zip(word1, word2):
            op.append(a)
            op.append(b)
        if w1>w2:
            op.extend(word1[w2:])
        elif w2>w1:
            op.extend(word2[w1:])
        return "".join(op)