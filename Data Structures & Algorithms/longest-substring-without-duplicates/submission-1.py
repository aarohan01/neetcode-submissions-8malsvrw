class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        ### Bruteforce ###
        # For each letter letter use bounded bruteforce and a hashset to check dupes
        # Set upper bound using R pointer and check using hashset by putting in from left pointer
        maxlen = 0
        
        for R in range(len(s)):
            curlen = 0
            hashset = set()
            for L in range(R,len(s)):

                if s[L] in hashset:
                    break
                
                curlen += 1
                maxlen = max(maxlen,curlen)
                hashset.add(s[L])

        return maxlen

                






            
        