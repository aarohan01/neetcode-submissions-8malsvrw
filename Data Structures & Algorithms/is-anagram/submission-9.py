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
        if ss != st:
            return False
        return True 
        '''

        ### Hashmap ###
        # convert to hashmap both strings and compare
        # Time : O(n) -> O(n) + O(n) + O(n) : convert s + convert t + compare
        # Space : O(1) or O(n) since only 26 letters

        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i],0)+1
            t_dict[t[i]] = t_dict.get(t[i],0)+1
        
        if s_dict == t_dict:
            return True 
        return False


        

