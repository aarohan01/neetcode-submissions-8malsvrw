class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        ### Bruteforce ###
        # For each letter use bounded bruteforce and a hashset to check dupes
        # Set upper bound using R pointer and check using hashset by putting in from left pointer
        # Time : O(n^2)
        # Space : O(m)
        '''
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
        '''

        ### Sliding window + Hashset ###
        # Idea is to keep adding elements to hashset until a dupe is discovered, if dupe is discovered need to shrink the window while
        # dupe is still in the set, then exapand again 
        # Time : O(n)
        # Space : O(m)

        L = 0
        maxlen = 0
        hashset = set()

        for R in range(len(s)):

                
            while s[R] in hashset:
                print(f'L : {L} Rem :{s[L]}')
                hashset.remove(s[L])
                L += 1
                print(f'L : {L}')
                


            hashset.add(s[R])
            print(f'Added : {s[R]}')

            maxlen = max(maxlen,R-L+1)

        return maxlen 


                






            
        