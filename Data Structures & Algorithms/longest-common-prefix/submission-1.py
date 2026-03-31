class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ### Solution 1 ###
        # Find minword and then based on that scan all the words 

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