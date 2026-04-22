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
        print(res, L, R)
        if res == False:
            return palindrome(s, L+1, R)[0] or palindrome(s, L, R-1)[0]

        return res

  