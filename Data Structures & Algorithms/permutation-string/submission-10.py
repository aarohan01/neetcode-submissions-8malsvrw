class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        ### Bruteforce ###
        # Sort string one and use sliding window to compare sorted window to sorted string one
        # Time : O(m*nlogn) -> for every letter m in s2 window length n of s1 sorted
        # Space : O(n) -> s1 and window of s2 
        '''
        sortedS1 = ''.join(sorted(s1))
        lenS1 = len(s1)
        print(f'S1 : {sortedS1}')
        L = 0
        for R in range(lenS1,len(s2)+1):

            window = ''.join(sorted(s2[L:R]))
            print(f'w - {window}')
            if window == sortedS1:
                return True
            L += 1
        return False
        '''


        ### Frequency Table + Sliding window ###
        # Use freq table to compare windows
        # This works but is not the most efficient due to slicing and then calculating freq for each window again 
        # n ( for s1) + n*m (for s2), similarly every slice will use memory 
        # Time : O(nm)
        # Space : O(1)
        ## Better version below ##
        '''
        def frequency(s: str) -> List:

            table = [0]*26
            for letter in s:
                table[ord(letter)-ord('a')] += 1
            return table

        s1table = frequency(s1)
        print(s1table)

        L=0
        for R in range(len(s1),len(s2)+1):
            s2table = frequency(s2[L:R])
            if s1table == s2table:
                return True
            L += 1
        return False
        '''

        ### Rolling freq table + sliding window ###
        # Same code better version below 
        '''
        s1table, s2table = [0]*26, [0]*26
        

        # S1 table 
        for l in s1:
            s1table[ord(l)-ord('a')] += 1
        print(s1table)
        
        L=0
        for R in range(len(s1),len(s2)+1):
            
            if L == 0:
                for l in s2[L:R]:
                    s2table[ord(l)-ord('a')] += 1
                print(s2table)
            
            else:
                s2table[ord(s2[R-1])-ord('a')] += 1


            if s1table == s2table:
                return True

            s2table[ord(s2[L])-ord('a')] -= 1
            L += 1
        return False
        '''


        ### Rolling freq table + sliding window ###
        # The idea is to keep window in freq table using R and removing freq using L 
        # We keep filling using R, if window too big shrink else check.
        # Can write using continue as well.
        # Time : O(n+m) or O(n)
        # Space : O(1)
        s1table, s2table = [0]*26, [0]*26

        # S1 table 
        for l in s1:
            s1table[ord(l)-ord('a')] += 1
        print(s1table)

        
        L=0
        #for R in range(len(s1),len(s2)+1):
        for R in range(len(s2)):
            
            # add freq of s2 window - Expand
            s2table[ord(s2[R])-ord('a')] += 1 

            # Window too large remove L freq and increament L for next - Shrink
            if R >= len(s1):
                s2table[ord(s2[L])-ord('a')] -= 1
                L += 1

            # Check window
            if s1table == s2table:
                return True

        return False
        
        


    

 


