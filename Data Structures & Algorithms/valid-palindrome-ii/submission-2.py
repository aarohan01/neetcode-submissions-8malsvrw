class Solution:
    def validPalindrome(self, s: str) -> bool:
        
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