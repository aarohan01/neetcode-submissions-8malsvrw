class Solution:
    def isPalindrome(self, s: str) -> bool:

        #Bruteforce 
        def isalphanum(l):

            return (ord('a') <= ord(l) <= ord('z')) | (ord('A') <= ord(l) <= ord('Z')) | (ord('0') <= ord(l) <= ord('9'))
        

        
        l = 0
        r = len(s) -1
        print(len(s))
        while l < r:
            print(l)
            print(r)
            if not isalphanum(s[l]):
                l += 1
                continue
            if not isalphanum(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
    
       
        