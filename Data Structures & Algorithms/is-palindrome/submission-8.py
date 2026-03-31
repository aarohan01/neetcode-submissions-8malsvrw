class Solution:
    def isPalindrome(self, s: str) -> bool:

        ### Bruteforce ###
        # covert to list, reverse and compare if same
        # O(n) + O(n) + O(n) i.e O(n) time complexity
        # O(n) space complexity


        ### Solution 1 ###
        # Use two pointers turning inwards and check if same if anytime not same return false
        # While two pointers meet check if not alpha num then increment or right or left else check pallindrome.
        # Handle edge of empty or one letter

        #Edge case 
        #Not required here but okay
        if len(s) <= 1:
            return True

        l = 0
        r = len(s)-1

        '''
        #This also works better way down.
        while l < r :

            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            if not self.isAlphaNum(s[r]):
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
        '''
        while l < r :

            if not self.isAlphaNum(s[l]):
                l += 1
            elif not self.isAlphaNum(s[r]):
                r -= 1
            else:    
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1

        return True

    def isAlphaNum(self, c: str) -> bool:
        
        '''
        if ((ord(c) >= ord('A') and ord(c) <= ord('Z')) or 
            (ord(c) >= ord('a') and ord(c) <= ord('z')) or 
            (ord(c) >= ord('0') and ord(c) <= ord('9'))) :
            return True 
        return False
        '''
        # Better way

        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
                
        