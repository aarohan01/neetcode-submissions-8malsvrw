class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        


        ### Comparing first and last word after sorting ###
        strs.sort()
        i = 0
        minlen = min(len(strs[0]),len(strs[-1]))
        while i < minlen and  strs[0][i] == strs[-1][i]:
            i += 1

        return strs[0][:i]