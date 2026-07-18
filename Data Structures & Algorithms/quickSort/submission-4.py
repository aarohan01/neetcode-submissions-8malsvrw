# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def quickSortHelper(self,pairs,s,e):

        ### Base condition ### 
        # If only one element left then return the array
        if e-s+1 <= 1:
            return pairs

        ### Solve the subproblem ###
        # Set a pivot and a filled pointer to track filled position in resultant array
        pivot = pairs[e]
        filled = s 

        # Iterate the array and fill the postions 
        for i in range(s,e+1):

            if pairs[i].key < pivot.key:
                pairs[filled],pairs[i] = pairs[i],pairs[filled]
                filled += 1 
        
        # Put the pivot in the middle / sorted place
        pairs[filled],pairs[i] = pairs[i],pairs[filled]

        # Recursion on filled and right part excluding the pivot that is at filled 
        self.quickSortHelper(pairs,s,filled-1)
        self.quickSortHelper(pairs,filled+1,e)
        
        




    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        
            

        self.quickSortHelper(pairs,0,len(pairs)-1)

        return pairs

        