class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        ### Bruteforce ###

        index = 0
        for i in range(len(s)):
            flag = False
            for j in range(index,len(t)):
                if s[i] == t[j]:
                    index = j+1
                    flag = True
                    break

            if not flag:
                return False 
            
        return True
    


                

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