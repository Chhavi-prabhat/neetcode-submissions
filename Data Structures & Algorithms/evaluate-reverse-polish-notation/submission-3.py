class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # while len(tokens) > 1:
        #     for i in range(len(tokens)):
        #         if tokens[i] in "+-*/":
        #             a = int(tokens[i-2])
        #             b = int(tokens[i-1])
        #             if tokens[i] == '+':
        #                 result = a + b
        #             elif tokens[i] == '-':
        #                 result = a - b
        #             elif tokens[i] == '*':
        #                 result = a * b
        #             elif tokens[i] == '/':
        #                 result = int(a / b)
        #             tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
        #             break
        # return int(tokens[0])
        tok = []
        for i in tokens:
            if i == "+":
                tok.append(tok.pop() + tok.pop())
            elif i == "-":
                a, b = tok.pop(), tok.pop()
                tok.append(b - a)
            elif i == "*":
                tok.append(tok.pop() * tok.pop())
            elif i == "/":
                a, b = tok.pop(), tok.pop()
                tok.append(int(b / a))  # FIXED for NeetCode
            else:
                tok.append(int(i))
        return tok[0]