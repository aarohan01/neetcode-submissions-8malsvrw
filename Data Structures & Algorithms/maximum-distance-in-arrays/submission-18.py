class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        

        ### Bruteforce ###
        # The main clue is all the arrays are sorted.
        # NOTE: the arrays are internally sorted but the outer array doesn't contains arrays sorted by inner contents
        # Thus the max of first array maybe bigger than min of 2nd array
        # So the first element is min and last is max in each array
        # So we can loop and subtract last element from each array with first element of other arrays
        '''
        maxdist = 0

        for i in range(len(arrays)):
            mini = arrays[i][0]
            maxi = arrays[i][-1]
            for j in range(i+1,len(arrays)):
                minj = arrays[j][0]
                maxj = arrays[j][-1]    

                # Since arrays are internally sorted but not externally array 2 can have smaller min than max of array 1
                # Thus we compare both ways                
                maxdist = max(abs(mini-maxj), abs(maxi-minj), maxdist)
        
        return maxdist
        '''


        ### Single scan ###
        # Instead of calculating min/max + distance with all other arrays
        # We can update a global variables maxdist, minprev -> mintill now, maxprev -> maxtill now
        # Calculate each arrays distance to these and update these as we move ahead
        # Time: O(n)
        # Space: O(1)

        maxdist = 0

        # Initially set to the first array
        minprev = arrays[0][0]
        maxprev = arrays[0][-1]

        for i in range(1,len(arrays)):
            
            # Current arrays min an max
            mincur = arrays[i][0]
            maxcur = arrays[i][-1]      

            # distance with the array with smallest min value and another array with the largest max value              
            maxdist = max(abs(minprev - maxcur), abs(maxprev - mincur), maxdist)

            # Update the min and max values
            minprev = min(minprev, mincur)
            maxprev = max(maxprev, maxcur)
        
        return maxdist


