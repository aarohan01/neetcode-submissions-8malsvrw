# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def merge(self,pairs,start,middle,end):

        #Conquer
        #To remember for merge : 3 pointers to track and swap and then again one loop to copy remaining

        l = 0 #left subarray
        r = 0 #right subarray
        x = start #parent subarray point in the original array

        L = pairs[start:middle+1]
        R = pairs[middle+1:end+1]

        #loop till reach end of one subarray
        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                pairs[x] = L[l]
                l += 1
            else :
                pairs[x] = R[r]
                r += 1
            x += 1

        #Copy remainging when one subarry is finished
        if l ==  len(L):
            pairs[x:end+1] = R[r:]
        else :
            pairs[x:end+1] = L[l:]
        
        return pairs



    def mergeSortHelper(self,pairs,start,end):
        
        #Divide 
        #Base Case
        if end - start + 1 <= 1:
            return pairs
        
        middle = (end+start)//2

        #Pass the entire array with just start and end point of sub-array
        self.mergeSortHelper(pairs,start,middle)
        self.mergeSortHelper(pairs,middle+1,end)

        return self.merge(pairs,start,middle,end)



    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        return self.mergeSortHelper(pairs,0,len(pairs)-1)
