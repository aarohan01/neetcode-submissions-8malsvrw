class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:


        ### Bruteforce ###
        # For each element try forming a subarray satisfying the condition.
        # Check if index is even or odd and check accordingly.
        # Start inner loop from index 1 to n-1 index
        '''
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
        '''


        ### Sliding window version 1 ###
        '''
        L = 0
        maxlen = 1
        prevsign = None
        for R in range(1,len(arr)):

            if arr[R] > arr[R-1]:
                cursign = -1
            elif arr[R] < arr[R-1]:
                cursign = 1
            else:
                L = R
                prevsign = None
                continue
            
            # In case other than 1st pair
            if prevsign is not None and cursign == prevsign:
                L = R-1 
                
            # In case of First pair and Other success case pairs
            prevsign = cursign

            maxlen = max(maxlen,R-L+1)
        return maxlen
        '''
        

        ### Sliding window version 2 ###
        # For each element :
        # There are four real conditions to check.
        # 1. prev sign '<' and matches '>' : Success
        # 2. prev sign '>' and matches '<' : Success
        # 3. Failures  - 1. same element 1st - reset 2. same element inbetween - Reset 3. sign not matching - reset 
        '''
        L = 0
        maxlen = 1
        prevsign = None

        for R in range(1,len(arr)):
            
            if arr[R] > arr[R-1] and prevsign == '<':
                maxlen = max(maxlen,R-L+1)
                prevsign = '>'
                print(f'R > R-1 R:{R} arr[R] : {arr[R]} max : {maxlen}')
            elif arr[R] < arr[R-1] and prevsign == '>':
                maxlen = max(maxlen,R-L+1)
                prevsign = '<'
                print(f'R < R-1 R:{R} arr[R] : {arr[R]} max : {maxlen}')
            else:
                ### Same element first or in between ###
                # Reset #
                if arr[R] == arr[R-1]:
                    L = R
                elif not prevsign:
                    maxlen = max(maxlen,R-L+1)
                    prevsign = '>' if arr[R] > arr[R-1] else '<'
                else:
                    ### Failure of sign ###
                    # Reset #
                    L = R - 1
                    prevsign = '>' if arr[R] > arr[R-1] else '<'
                
                print(f'R == R-1 R:{R} arr[R] : {arr[R]} max : {maxlen}')
    
        return maxlen
        '''

        ### Sliding window version 3 ###

        L = 0
        maxlen = 1
        prevsign = None

        for R in range(1,len(arr)):

            ### Failure same - reset ###
            if arr[R] == arr[R-1]:
                L = R
                prevsign = None
            
            else :

                cursign = '>' if arr[R] > arr[R-1] else '<'

                if prevsign == None:
                    # First element of subarray not same
                    prevsign = cursign 
                elif cursign != prevsign:
                    prevsign = cursign 
                elif cursign == prevsign:
                    ### Reset ###
                    L = R - 1
                    prevsign = cursign 
                
            maxlen = max(maxlen, R-L+1)

        return maxlen 
                









                
            


                

                







                


                



                






                    
                    


        