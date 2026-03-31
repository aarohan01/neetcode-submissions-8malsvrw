class Solution:

    def __init__(self):
        self.delim = ','
        self.final = '#'

    def encode(self, strs: List[str]) -> str:

        
        res = [ str(len(s)) + self.delim + s for s in strs ]
        print(f'Encoded : {res}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:


        res = []

        L = 0
        R = len(s)

        while L < R:
            i = L+1
            
            while s[i] != self.delim:
                i += 1
            print(f'L:{L} i:{i} len: {s[L:L+i]}')
            wlen = int(s[L:i])
            res.append(s[i+1:i+wlen+1])
            print(res)
            L = i + wlen + 1
        
        return res
            


