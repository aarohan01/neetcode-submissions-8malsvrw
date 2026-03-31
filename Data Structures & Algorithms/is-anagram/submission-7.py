class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ### Bruteforce ###
        # Sort both strings then loop 
        # Time : O(nlogn) -> O(nlogn) + O(n) : sorting + loop
        # Space : O(n)
        '''
        if len(s) != len(t):
            return False

        ss = sorted(s)
        st = sorted(t)
        for i in range(len(s)):
            if ss[i] != st[i]:
                return False 
        return True
        '''

        ### Hashmap ###
        # convert to hashmap both strings and compare
        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i,0)+1
        
        t_dict = {}
        for i in t:
            t_dict[i] = t_dict.get(i,0)+1
        
        if s_dict == t_dict:
            return True 
        return False


        

