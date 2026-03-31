class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ### Bruteforce ###
        # 

        minlen = float('inf')
        minword = None
        for w in strs:
            if len(w) < minlen:
                minlen = len(w)
                minword = w
        print(f'w:{minword} l:{minlen}')

        word =''
        for i,s in enumerate(minword):
            for w in strs:
                if w[i] == s:
                    continue
                else:
                    return word
            word += s
        
        return word