### Bruteforce ###
# For min if only stack function allowed to use then pop every element into temp while calculating min
# then append again.
# Time : O(n)
# Space : O(n) aux
'''
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
'''
### Two Stack ###
# Use two stacks, one maintains value and one maintains minvalue
# While pushing just check if stack empty or less than previous min value and insert in minstack accordingly
# Time : O(1)
# Space : O(n)
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        
        if not self.stack or val < self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])
        self.stack.append(val)


    def pop(self) -> None:

        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
'''
### One Stack Trick ###
# The trick is to store difference between val and minval into the stack.
# Store diff first and then update minval, only caveat is if stack empty then set the minval to val 
# To get top -> if +ve then minval + val else minval 
# To pop -> if the val is -ve that means there was minval update so minval - val is minval else nothing 
# Time : O(n)
# Space : O(1)
class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = float('inf')

    def push(self, val: int) -> None:
        
        # If empty
        if not self.stack:
            self.minval = val

        self.stack.append(val - self.minval)

        # After every push update minval 
        self.minval = min(val,self.minval)


    def pop(self) -> None:
        
        val = self.stack[-1]
        if val < 0:
            self.minval -= val
        self.stack.pop()
        

    def top(self) -> int:
        
        val = self.stack[-1]
        if val > 0:
            return val + self.minval
        else:
            return self.minval
        

    def getMin(self) -> int:
        return self.minval
        
