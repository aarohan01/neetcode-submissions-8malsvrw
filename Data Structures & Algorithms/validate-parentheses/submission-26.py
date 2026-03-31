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

        ### Stack  and Hashmap ###
        # Put open brackets in the stack, if close bracket then check if stack top is its pair else false
        # At the end if stack is empty then true else false
        # Time : O(n)
        # Space : O(n)
        ## Better way to write below ##
        '''
        stack = []
        hashmap = { '}':'{', ')':'(', ']':'[' }
        for bracket in s:
            if bracket in '([{':
                stack.append(bracket)
            elif b in '}])':
                print(f'b:{bracket} stack:{stack}')
                if not stack or stack.pop() != hashmap[bracket]:
                    return False
        
        if not stack:
            return True
        return False
        '''

        ### Stack and Hashmap ###
        # If the bracket is in hashmap then check if stack is not empty and top is same as pair
        # If not in hashmap push to stack 
        # At the end if stack is empty then True else False 
        # Time : O(n)
        # Space : O(n)
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
            
        
        if not stack:
            return True
        return False



            








        