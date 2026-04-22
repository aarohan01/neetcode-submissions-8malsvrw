class Solution:
    def validPalindrome(self, s: str) -> bool:


        ### NOT THE SOLUTION ###
        # This passes all the testcases on neetcode but doesn't when more testcases are generated in ChatGPT
        '''
        skip = 1
        L, R = 0, len(s)-1

        while L < R:

            if s[L] != s[R]:

                if skip == 1:
                    skip -= 1
                    if s[R-1] == s[L] and s[R-2] == s[L+1]:
                        R -= 1
                    else:
                        L += 1
                    continue
                else:
                    return False
            L += 1
            R -= 1
        return True
        '''

        ### Two pointers and sorting ###
        L, R = 0, len(s)-1

        while L < R:

                if  s[L] != s[R]:
                    sl, sr = s[L+1:R+1], s[L:R]
                    return sl == sl[::-1] or sr == sr[::-1]
                else:
                    L += 1
                    R -= 1
        
        return True

    

        ### Two Pointers + recursion 1 ###
        # check if string is pallindrome using two pointers
        # If its not check once again shifting left and right
        ## Cleaner verion below
        ## Time: O(n)
        ## Space: O(1)
        '''
        def palindrome(st: str, L, R) -> bool:
            
            while L < R:
                if  st[L] != st[R]:
                    return [False, L, R]
                else:
                    L += 1
                    R -= 1

            return [True, L, R]

        
        L, R = 0, len(s)-1
        res, L, R = palindrome(s, L, R)
        if res:
            return res
        else:
            return palindrome(s, L+1, R)[0] or palindrome(s, L, R-1)[0]
        '''
        
        ### Two pointer + recursion ###
        # Check palindrome normally if false check once again wih shifting L or R
        # The recursive branch will not be long since we only call the function when first false is detected
        # Thus either branch will soon return False if its wrong
        # Time: O(n)
        # Space: O(1)
        def palindrome(L, R) -> bool:
            
            while L < R:
                if  s[L] != s[R]:
                    return False
                else:
                    L += 1
                    R -= 1

            return True

        
        L, R = 0, len(s)-1
        while L < R:

                if  s[L] != s[R]:
                    return palindrome(L+1,R) or palindrome(L, R-1)
                else:
                    L += 1
                    R -= 1
        
        return True




