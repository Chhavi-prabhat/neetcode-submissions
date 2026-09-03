class MinStack:

    def __init__(self):
        self.stack=[]
        self.top_index=-1
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_index+=1
        
    def pop(self) -> None:
        self.stack.pop()
        self.top_index-=1

    def top(self) -> int:
        if self.top_index==-1:
            return -1
        else:
            return self.stack[self.top_index]

    def getMin(self) -> int:
        return min(self.stack)
        
