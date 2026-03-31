class Solution:
    def isPalindrome(self, s: str) -> bool:

        #Bruteforce 
        def isalphanum(l):

            return (ord('a') <= ord(l) <= ord('z')) | (ord('A') <= ord(l) <= ord('Z')) | (ord('0') <= ord(l) <= ord('9'))
        

        forward = [ l.lower() for l in s if isalphanum(l) ]
        backward = [ l.lower() for l in s[::-1] if isalphanum(l)]

        print(forward)
        print(backward)
        return forward == backward