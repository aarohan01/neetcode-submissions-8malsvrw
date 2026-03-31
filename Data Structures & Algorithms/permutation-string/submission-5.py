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


    

 


