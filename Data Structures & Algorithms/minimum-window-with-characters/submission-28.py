class Solution:
    
    def freqtable(self,word,table):

        for w in word:
            table[w] = table.get(w,0) +1
        return table


    def minWindow(self, s: str, t: str) -> str:
        

        ### Bruteforce ###
        # Why not sorting t and checking window of s by sorting and comparing ?
        # coz can't do sorted(t) in sorted(window(s)) due to duplicated thus frequency table required
        # Idea : create freq table of t and use bounded bruteforce using freq table of window and compare if
        # the all elements of t are in window table and freq is lower than equal to window table 
        # Update the minlen and minword based on that.
        # Time: O(n^2m) -> Loop is n^2 and every loop we check m characters (worst case) of t.
        # Space: O(n + m)
        # n -> len(s), m -> len(t)
        '''
        minlen = float('inf')
        minword = ""
        
        freqt = self.freqtable(t,{})
        freqtlen = len(freqt)
        #print(freqt)

        for i in range(len(s)):
            freqw = {}
            for j in range(i,len(s)):
    
                freqw = self.freqtable(s[j],freqw)
                
                counter = 0
                for k,v in freqt.items():
                    if k in freqw and v <= freqw[k]:
                        counter += 1

                if counter == freqtlen and j-i+1 < minlen:
                    minlen = j-i+1
                    minword = s[i:j+1]

        return minword
        '''
        ### Sliding Window ###
        
        minlen = float('inf')
        minword = ""
        
        freqt = self.freqtable(t,{})
        freqtlen = len(freqt)


        L = 0

        freqw = {}
        counter = 0
        for R in range(len(s)):
            #print(f'R:{R} {s[L:R+1]}')
            # Expand
            freqw = self.freqtable(s[R],freqw)

            # Check 
            ## Don't need to check the counter everytime if its equal then only update counter
            ## This way even if more frequent it doesn't get changed.
            
            #counter = 0
            #for k,v in freqt.items():
                #if k in freqw and v <= freqw[k]:
                    #print(f'k :{k} {freqw}')
                    #counter += 1
            
            if s[R] in freqt and freqw[s[R]] == freqt[s[R]]:
                counter += 1
            
            #print(f'count:{counter}')
            
            # Shrink 
            while counter == freqtlen:
                if R-L+1 < minlen:
                    minlen = R-L+1
                    minword = s[L:R+1]
                #print(f'minword:{minword}')
                #print(f'Removing L:{L} {s[L]}')

                freqw[s[L]] -= 1

                if s[L] in freqt and freqw.get(s[L],0) < freqt[s[L]]:
                    counter -= 1
                L += 1
        return minword
         





            






                
            







