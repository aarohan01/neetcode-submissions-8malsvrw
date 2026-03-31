class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        ### Solution 1 ###
        s_set = set(s)
        t_set = set(t)

        return s_set == t_set and len(s) == len(t)
        '''

        ### Solution 2 ###
        ### Intuition : create two hashmaps for each string for each letter compare ###
        s_dict = dict()
        for i in s:
            if i in s_dict.keys():
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        t_dict = dict()
        for i in t:
            if i in t_dict.keys():
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        print(s_dict)
        print(t_dict)
        
        if s_dict == t_dict:
            return True
        else:
            return False
        