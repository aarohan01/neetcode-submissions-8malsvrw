class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ### Bruteforce ###
        # Time: O(n^2)
        # Space: O(1)
        '''
        for i in range(len(arr)-1):
            maxnum = float('-inf')
            for j in range(i+1,len(arr)):

                maxnum =  max(maxnum, arr[j])

            arr[i] = maxnum
        arr[-1] = -1
        return arr
        '''

        maxnum = arr[-1]
        for i in range(len(arr)-2,-1,-1):

            curnum = arr[i]
            arr[i] = maxnum
            maxnum = max(maxnum, curnum)
        
        arr[-1] = -1
        return arr

