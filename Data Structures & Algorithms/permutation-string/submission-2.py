class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        ### Bruteforce ###
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
    

 


