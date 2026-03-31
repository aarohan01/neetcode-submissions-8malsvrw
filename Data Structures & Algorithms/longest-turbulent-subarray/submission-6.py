class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:


        ### Bruteforce ###
        # For each element try forming a subarray satisfying the condition.
        # Check if index is even or odd and check accordingly.
        # Start inner loop from index 1 to n-1 index


        maxlen = 1
        for L in range(len(arr)):
            # To denote first pair status
            prevsign = None
            for R in range(L+1,len(arr)):
                
                # General cases 
                if arr[R] > arr[R-1]:
                    cursign = -1
                elif arr[R] < arr[R-1]:
                    cursign = 1
                else:
                    break 

                # In case other than 1st pair
                if prevsign is not None and cursign == prevsign:
                    break 
                
                # In case of First pair and Other success case pairs
                prevsign = cursign  

                maxlen = max(maxlen,R-L+1)
            
        return maxlen


                
            


                

                







                


                



                






                    
                    


        