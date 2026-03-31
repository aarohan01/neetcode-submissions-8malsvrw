class Solution:
    def isValid(self, s: str) -> bool:

        ### Bruteforce ###
        # Repeatedly remove bracket pairs from the string while they exist
        # Return True is empty else false
        # Time : O(n^2)
        # Space : O(1)
        '''
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        
        if not s:
            return True 
        return False
        '''

        ### Stack ###
        stack = []
        hashmap = { '}':'{', ')':'(', ']':'[' }
        for b in s:
            if b in '([{':
                stack.append(b)
            elif b in '}])':
                print(f'b:{b} stack:{stack}')
                if not stack or stack.pop() != hashmap[b]:
                    return False
        
        if not stack:
            return True
        return False

            








        