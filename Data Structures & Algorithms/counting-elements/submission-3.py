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

        ### Hashset ###
        # Membership check for hashset is O(1)
        hashset = set(arr)
        count = 0
        for n in arr:
            if (n+1) in hashset:
                count += 1
        return count 



