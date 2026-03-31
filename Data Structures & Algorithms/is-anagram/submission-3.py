class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        ### Solution 1 ###
        s_set = set(s)
        t_set = set(t)

        return s_set == t_set and len(s) == len(t)
        '''

        '''
        ### Solution 2 ### WORKS and is correct intuition, execution could be better ###
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
        
        '''
        ### Solution 3 ### 
        ### Same as Solution 2 but better execution ###
        ### First return false if not same size, then only check in hashmap ###

        if len(s) != len(t):
            return False
        
        #Now we know that lenght will be same, some combining loop to create hashmap
        s_dict, t_dict = {} , {}
        for i in range(len(s)):

            '''
            if s[i] in s_dict.keys() :
                s_dict[s[i]] += 1
            s_dict[s[i]] = 1 
            '''
            s_dict[s[i]] = s_dict.get(s[i],0) + 1
            t_dict[t[i]] = t_dict.get(t[i],0) + 1

        return s_dict == t_dict 