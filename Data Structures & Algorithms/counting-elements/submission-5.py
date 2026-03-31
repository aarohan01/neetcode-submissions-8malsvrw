class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        ### Bruteforce ###
        # Time : O(n^2)
        # Space : O(1)
        '''
        count = 0

        for n in arr:

            if (n + 1) in arr:
                count += 1

        return count  
        '''

        ### Hashset ### Optimal w.r.t time ###
        # Membership check for hashset is O(1)
        # Time : O(n)
        # Space : O(n)
        '''
        hashset = set(arr)
        count = 0
        for n in arr:
            if (n+1) in hashset:
                count += 1
        return count 
        '''

        ### Sort and count ### Optimal w.r.t space but depends ###
        arr.sort()
        count = 0
        copy = 1
        for i in range(len(arr)-1):
            
            if arr[i] != arr[i+1]:
                if arr[i+1] - arr[i] == 1:
                    count += copy
                copy = 1
            else:
                copy += 1

        return count
