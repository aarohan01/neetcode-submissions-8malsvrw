class Solution:
    def isValid(self, s: str) -> bool:
        
        # Bruteforce 



        # Solution 1 #
        # first check if length is even, if not return false.
        # Use two pointers from different ends and if they are not opposite return false



        stack = []
        hashmap = {'}':'{',')':'(',']':'['}
        '''
        for bracket in s:
            if bracket in hashmap:
                if stack and stack[-1] == hashmap[bracket] :
                    stack.pop()
                else :
                    return False
            else:
                stack.append(bracket)
        '''

        for bracket in s:
            if bracket not in hashmap:
                stack.append(bracket)
            else :
                if stack and stack[-1] == hashmap[bracket] :
                    stack.pop()
                else :
                    return False

        if len(stack) == 0 :
            return True
        return False

