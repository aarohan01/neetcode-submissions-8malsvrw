class Solution:
    def isPalindrome(self, s: str) -> bool:

        ### Bruteforce ###
        # covert to list, reverse and compare if same
        # O(n) + O(n) + O(n) i.e O(n) time complexity
        # O(n) space complexity


        ### Solution 1 ###
        # use two pointers turning inwards and check if same if anytime not same return false
        # Handle edge of empty or one letter

        #Edge case 
        if len(s) <= 1:
            return True

        l = 0
        r = len(s)-1

        while l < r :

            if not self.isAlphaNum(s[l]):
                print('L')
                l += 1
                continue
            if not self.isAlphaNum(s[r]):
                print('R')
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True

    def isAlphaNum(self, c: str) -> bool:
            
        if ((ord(c) >= ord('A') and ord(c) <= ord('Z')) or 
            (ord(c) >= ord('a') and ord(c) <= ord('z')) or 
            (ord(c) >= ord('0') and ord(c) <= ord('9'))) :
            return True 
        return False
        