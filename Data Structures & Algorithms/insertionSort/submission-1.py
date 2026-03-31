# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    # Implementation of Insertion Sort
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []   # To store the intermediate states of the array
        if len(pairs) > 0:
            res.append(pairs[:]) #Why not pairs ? because tha is self referential so all are updated as status changes
        for i in range(1,n):
            j = i - 1

            # Move elements that are greater than key one position ahead
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            
            # Clone and save the entire state of the array at this point
            res.append(pairs[:])
            

        return res
