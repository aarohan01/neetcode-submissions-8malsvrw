from math import ceil
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        ### Bruteforce ###
        '''
        count = 0
        for L in range(len(arr)-k+1):
            print(f'L {L}- sum :{arr[L]}')
            asum = arr[L]
            for R in range(L+1, min(len(arr), L+k)):
                asum += arr[R]
                print(f'R {R}- sum :{arr[R]}')
            

            avg = asum / k 
            print(asum,avg)
            if avg >= threshold:
                count += 1
        return count
        '''
        # OR 
        count = 0
        L = 0
        for R in range(k-1, len(arr)):
            print(f'R {R}- sum :{arr[R]}')
            asum = arr[R]
            for L in range(R-k+1,R):
                asum += arr[L]
                print(f'L {L}- sum :{arr[L]}')
            

            avg = asum / k 
            print(asum,avg)
            if avg >= threshold:
                count += 1
        return count
