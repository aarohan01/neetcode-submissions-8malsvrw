class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ### Bruteforce ###
        # Sort both strings then loop 
        # Time : O(n^2)
        # Space : O(1)

        if len(s) != len(t):
            return False

        ss = sorted(s)
        st = sorted(t)
        for i in range(len(s)):
            if ss[i] != st[i]:
                return False 
        return True
        

