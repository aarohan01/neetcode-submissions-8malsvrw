class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        ### Bruteforce ###
        # For each letter letter use bounded bruteforce and a hashset to check dupes
        # Set upper bound using R pointer and check using hashset by putting in from left pointer
        maxlen = 0
        
        for L in range(len(s)):
            hashset = set()
            for R in range(L,len(s)):

                if s[R] in hashset:
                    break
                
                curlen = R-L+1
                maxlen = max(maxlen,curlen)
                hashset.add(s[R])

        return maxlen

                






            
        