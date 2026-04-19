class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:


        nword = []

        w1, w2 = 0,0

        
        while w1 < len(word1) and w2 < len(word2):


            if len(nword) % 2 == 0:
                nword.append(word1[w1])
                w1 += 1
            else:
                nword.append(word2[w2])
                w2 += 1
            
        
        while w1 < len(word1):
            nword.append(word1[w1])
            w1 += 1

        while w2 < len(word2):
            nword.append(word2[w2])
            w2 += 1 

        return ''.join(nword)           

        