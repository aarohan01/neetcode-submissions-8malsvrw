class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        

        ### Bruteforce ###
        # The main clue is all the arrays are sorted 
        # So the first element is min and last is max in each array
        # So we can loop and subtract last element from each array with first element of ohter arrays
        '''
        maxdist = 0

        for i in range(len(arrays)):
            mini = arrays[i][0]
            maxi = arrays[i][-1]
            for j in range(i+1,len(arrays)):
                minj = arrays[j][0]
                maxj = arrays[j][-1]                    
                maxdist = max(abs(mini-maxj), abs(maxi-minj), maxdist)
        
        return maxdist
        '''


        ### Single scan ###
        # Instead of calculating min/max + distance with all other arrays
        # We can update a global variable continuously in one scan 
        maxdist = 0

        for i in range(1,len(arrays)):
            minprev = arrays[i-1][0]
            maxprev = arrays[i-1][-1]
            mincur = arrays[i][0]
            maxcur = arrays[i][-1]                    
            maxdist = max(abs(minprev - maxcur), abs(maxprev - mincur), maxdist)
        
        return maxdist


