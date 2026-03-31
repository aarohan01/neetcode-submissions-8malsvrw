class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        ###  Bruteforce ###

            



        ### Stack ###
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
            




