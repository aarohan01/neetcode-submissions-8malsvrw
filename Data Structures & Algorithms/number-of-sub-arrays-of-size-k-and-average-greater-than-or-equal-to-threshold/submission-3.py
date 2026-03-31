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
        '''
        count = 0
        L = 0

        for R in range(k, len(arr)+1):
            asum = 0
            for L in range(R-k,R):

                asum += arr[L]
                print(f'L {L}- sum :{arr[L]}')
            
            avg = asum / k 
            print(asum,avg)
            if avg >= threshold:
                count += 1
        return count
        '''


        ### Sliding Window ###
        # Use only one pointer and a sliding window 
        count = 0
        asum = 0
        threshold *= k
        for R in range(len(arr)):

            asum += arr[R]
            print(f'Add {arr[R]}')

            if R - k + 1>= 0:

                if asum >= threshold:
                    count += 1
                asum -= arr[R - k + 1]

        return count


        



