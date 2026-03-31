class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        tmp = []
        #hashmap = {'/':/, '*':*, '+':+, '-':-}
        for i in tokens:

            if i not in '/*+-':
                tmp.append(i)
            else:
                x,y = int(tmp.pop()),int(tmp.pop())
                if i == '/':
                    res = y/x 
                elif i == '*':
                    res = y*x 
                elif i == '+':
                    res = y+x
                else: 
                    res = y-x
                print(f'{x} {i} {y} = {res}')
                tmp.append(res)
        return int(tmp[-1])




