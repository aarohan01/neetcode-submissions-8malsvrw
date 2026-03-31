class Solution:
    
    # Check out Tricks & Issues - String #

    ### Bruteforce ###
    # Special edge cases for empty, one string and no string 
    # Else use a delimiter 
    def __init__(self):
        self.delim = '#*#*#'
        self.empty = '<EMPTY>'
        self.single_empty = '<SINGLE_EMPLTY>'

    def encode(self, strs: List[str]) -> str:

        if strs == []:
            return self.empty
        
        if strs == ['']:
            return self.single_empty

        return self.delim.join(strs)

    def decode(self, s: str) -> List[str]:

        if s == self.empty:
            return []
        
        if s == self.single_empty:
            return ['']
        
        return s.split(self.delim)
