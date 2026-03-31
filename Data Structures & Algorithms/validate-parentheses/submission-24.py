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

        for bracket in s:

            if bracket in hashmap:

                if stack and stack[-1] == hashmap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        if stack:
            return False
        return True

            








        