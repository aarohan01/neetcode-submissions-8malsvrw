class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        ### Bruteforce ###
        # Loop though the s and for each letter check if char exists in t
        # and check next char exits in t after the previous chars index, repeatedly 
        # Count all the characters found 
        # If count is equal to length of s then we found all characters return True else false
        # Time: O(s*t) -> we loop through all char of s always hence if no chars found loop though t everytime
        # Space: O(1)
        '''
        index = 0
        count = 0
        for i in s:
            print(i)
            for j in range(index,len(t)):
                if i == t[j]:
                    index = j+1
                    count += 1
                    break
            
        return count == len(s)
        '''

        ### Improved loop check ###
        # Instead of checking count in the loop check if char found if not immediatedly return False
        # Time: O(s + t) -> we only check parts of t or atmost entire t once.
        # Space: O(1)
        '''
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
        '''


                

        ### Two Pointers ###
        # Use two pointers one poiter for s and another for t
        # Loop t to check character in s using l pointer, if found increment pointer
        # if l become equal to len(s) then we have all chars.
        # Check the break condition before in the loop to avoid edge case of "".
        # Time: O(t + s)
        # Space : O(1)
        
        l = 0

        for i in range(len(t)):
            
            if l >= len(s):
                break

            if t[i] == s[l]:
                l += 1


        if l == len(s):
            return True
        return False
        