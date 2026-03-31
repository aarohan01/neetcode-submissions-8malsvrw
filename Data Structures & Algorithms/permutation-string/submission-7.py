class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        ### Bruteforce ###
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
        s1table, s2table = [0]*26, [0]*26
        

        # S1 table 
        for l in s1:
            s1table[ord(l)-ord('a')] += 1
        print(s1table)

        
        L=0
        #for R in range(len(s1),len(s2)+1):
        for R in range(len(s2)):

        
            s2table[ord(s2[R])-ord('a')] += 1 
            print(R)
            print(s2table[:4])


            if R >= len(s1):
                print(f'L {L}')
                s2table[ord(s2[L])-ord('a')] -= 1
                L += 1

            if s1table == s2table:
                return True

        return False
        


    

 


