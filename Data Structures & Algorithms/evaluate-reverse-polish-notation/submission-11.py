class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        ###  Bruteforce ###
        # while tokens exits do the operation on the previous two integers and recreate tokens
        # Time : O(n^2)
        # Space : O(n)   -> concatenating create new list 
        while len(tokens) > 1:
            for t in range(len(tokens)):
                tk = tokens[t]
                if tk in ('/','*','+','-'):
                    x,y = int(tokens[t-1]), int(tokens[t-2])
                    if tk == '/':
                        res = int(y / x) 
                    elif tk == '*':
                        res = y * x 
                    elif tk == '+':
                        res = y + x
                    else: 
                        res = y - x

                    print(f'{y} {tk} {x} = {res}')
                    tokens = tokens[:t-2] + [str(res)] + tokens[t+1:]
                    print(tokens)
                    break
        
        return int(tokens[0])

            
        ### Stack ###
        # Use stack if not operands than push to stack else pop and do operatoins and push 
        # Time : O(n)
        # Space : O(n)
        
        stack = []

        for t in tokens:
            res = 0
            if t in ['/','*','+','-']:
                x , y = stack.pop(), stack.pop()
                if t == '/':
                    res = int(y / x) 
                elif t == '*':
                    res = y * x 
                elif t == '+':
                    res = y + x
                else: 
                    res = y - x
                print(f'{y} {t} {x} = {res}')
                stack.append(int(res))
            else:
                stack.append(int(t))

        return stack[0]
            




