class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ### Solution 1 : minword and horizontal scanning ###
        ## Better version below##
        # Find minword and then based on that scan all the words horizontally 
        # Time : O(n*m) n->words m->shortes word
        # Space : O(1)
        '''
        minlen = float('inf')
        minword = None
        for w in strs:
            if len(w) < minlen:
                minlen = len(w)
                minword = w
        print(f'w:{minword} l:{minlen}')

        windex = 0
        for i,s in enumerate(minword):
            for w in strs:
                if w[i] == s:
                    continue
                else:
                    return minword[:windex]
            windex += 1
        
        return minword[:windex]
        '''


        ### Horizontal Scanning ###
        # There is no need for finding min word, use the first word, we can just break instead

        if not strs:
            return strs

        word = strs[0]

        for w in range(len(word)):
            for s in range(1,len(strs)):
                
                ## Out of bounds get avoided because OR checks conditions in order
                # If first codition is False, 2nd isn't even execute.
                if w >= len(strs[s]) or word[w] != strs[s][w]:
                    return word[:w]
                    
        return word
                    


        


