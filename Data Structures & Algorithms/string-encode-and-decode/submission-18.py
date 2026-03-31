class Solution:

    def __init__(self):
        self.delim = ','
        self.final = '#'

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ''
        
        lengths = [ str(len(s)) for s in strs ]
        
        res =  self.delim.join(lengths) + self.final +  ''.join(strs)
    
        print(res)
        return res

    def decode(self, s: str) -> List[str]:

        
        if not s:
            return []

        length, words  = s.split(self.final,1)
        print(length)
        print(words)

        lens = length.split(self.delim)

        res = []

        L = 0

        for i in lens:

            res.append(words[L:L + int(i)])
            L += int(i)
        print(res)
        return res

