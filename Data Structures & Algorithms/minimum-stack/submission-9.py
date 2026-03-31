### Bruteforce ###

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)   

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        #return min(self.stack)

        #OR is stack only operations allowed 
        temp = []
        mini = float('inf')
   
        while self.stack:
            s = self.stack.pop()
            mini = min(mini,s)
            temp.append(s)

        
        for s in range(len(temp)-1,-1,-1):
            self.stack.append(temp[s])
        
        return mini


