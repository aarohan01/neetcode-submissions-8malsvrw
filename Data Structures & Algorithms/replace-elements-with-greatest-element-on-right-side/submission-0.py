class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ### Bruteforce ###
        for i in range(len(arr)-1):
            maxnum = float('-inf')
            for j in range(i+1,len(arr)):

                maxnum =  max(maxnum, arr[j])

            arr[i] = maxnum
        arr[-1] = -1
        return arr