class Solution:
    
    # Check out Tricks & Issues - String #

    ### Bruteforce ###
    # Special edge cases for empty, one string and no string 
    # Else use a delimiter 
    '''
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
    '''

    ### Solution 1 # Correct and efficient but not preferred ###
    # Record length of the each string and delimit the lengths plus a final delimiter 
    # Ex:  ['abc','xyz'] -> 3,3#abcxyz 
    # Time : O(m) where m is the number of characters total in n strings
    # Space : O(m + n)  -> Here at the same time the lengths are in the memory along with the characters
    '''
    def __init__(self):
        self.delim = ','
        self.final = '#'

    def encode(self, strs: List[str]) -> str:
        
        # Output : 5,5,#HelloWorld
        slens = []

        #### IMP : Correct but very inefficient ###
        #e = ''
        #for s in strs:
        #    e += str(len(s)) + self.delim
        
        for s in strs:
            slens.append(str(len(s)))
        

        e = self.delim.join(slens) + self.final + ''.join(strs)

        print(e)
        return e




    def decode(self, s: str) -> List[str]:

        d = []
        header, strs = s.split('#',1)
        
        slens = [ int(i) for i in header.split(',') if i != '']
        print(slens)
        
        wlen = 0
        for sl in slens:
            d.append(strs[wlen: wlen + sl])
            wlen += sl 
        
        
        return d
    '''

    ### Solution 2 - Preferred as cleaner and streamable also don't have to decode the lengths beforehand ###
    # Record length and delim before every word
    # Ex : ['abc','xyz'] -> 3#abc3#xyz
    def __init__(self):
        self.delim = '#'


    def encode(self, strs: List[str]) -> str:
        
        
        # Output : 5#Hello5#World

        #### IMP : Correct but very inefficient ###
        #e = ''
        #for s in strs:
        #    e += str(len(s)) + self.delim
        
        strings = []
        for s in strs:
            strings.append(str(len(s)) + self.delim + s)

        e = ''.join(strings)


        print(e)
        return e




    def decode(self, s: str) -> List[str]:

        d = []
        #print(len(s))
        
        ### Scan/Parse using index walk ###
        i = 0
        while i < len(s):
            j = i
            
            while s[j] != self.delim:
                j += 1
            
            wlen = int(s[i:j])
            d.append(s[j+1: j+1+wlen])
            i = j+1+wlen

                

        
        return d
        


