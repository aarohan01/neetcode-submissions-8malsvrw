# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:


    def merge(self, pairs: List[Pair],s,m,e):
        
        #Copy to temp arrays
        L = pairs[s:m+1]
        R = pairs[m+1:e+1]    ####### Not e , e+1 or m+1: 

        #Index to track halves and og array,
        l = 0
        r = 0
        x = s

        #check and swap till one array reaches end, make entry in the parent array
        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                pairs[x] = L[l]
                l += 1
            else :
                pairs[x] = R[r]
                r += 1
            x += 1

        
        #concatenate remaining elements in parent array
        if l < len(L):
            pairs[x:e+1] = L[l:]
        elif r < len(R):
            pairs[x:e+1] = R[r:]

        
        '''
        while l < len(L):
            pairs[x] = L[l]
            l += 1
            x += 1
        while r < len(R):
            pairs[x] = R[r]
            r += 1
            x += 1
        '''        





    def mergeSortHelper(self, pairs: List[Pair],s,e):

        if e-s+1 <= 1:
            return pairs
        
        m = (e+s)//2

        self.mergeSortHelper(pairs,s,m)
        self.mergeSortHelper(pairs,m+1,e)

        self.merge(pairs,s,m,e)
        
        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        return self.mergeSortHelper(pairs,0,len(pairs)-1)

        






