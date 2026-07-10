class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        ### Bruteforce ###

        index = 0
        count = 0
        for i in range(len(s)):
            for j in range(index,len(t)):
                if s[i] == t[j]:
                    index = j+1
                    count += 1
                    break
            
        return count == len(s)
    


                

        ### Two Pointers ###
        # Use two pointers 
        '''
        l = 0

        for i in range(len(t)):
            
            if l >= len(s):
                break
            if t[i] == s[l]:
                l += 1


        if l == len(s):
            return True
        return False
        '''