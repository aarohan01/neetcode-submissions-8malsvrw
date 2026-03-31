class Solution:

    def __init__(self):
        self.delimiter = '#1#2#3#4#'

    def encode(self, strs: List[str]) -> str:
        
        if not strs:
            return '<EMPTY_STR1>'
        
        if len(strs) == 0:
            return '<EMPTY_STR2>'

        res = self.delimiter.join(strs)
        print(res)
        return res


    def decode(self, s: str) -> List[str]:

        if s == '<EMPTY_STR1>':
            return []
        
        if s == '<EMPTY_STR2>':
            return ['']
        
        res = s.split(self.delimiter)
        print(res)
        return res
