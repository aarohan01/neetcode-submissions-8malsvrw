class Solution:
    def trap(self, height: List[int]) -> int:


        ### Bruteforce ###
        # For each element i find the the tallest on left and right side higher than itself
        # the area over it is min of those height - height of i
        '''
        trapped = 0
        n = len(height)
        for i in range(1,n-1):
            
            leftmax, rightmax = 0, 0
            # Using loop instead of max() to save memeory
            for j in range(i):
                leftmax = max(leftmax,height[j])

            for j in range(i+1,n):
                rightmax = max(rightmax,height[j])

            if min(leftmax,rightmax) > height[i]:
                trapped += min(leftmax,rightmax) - height[i]
            
            print(f'i:{i} l:{leftmax} r:{rightmax} t:{trapped}')

        return trapped
        '''


        ### Prefix and Suffix ###
        # Instead of calculating max on left and right each time we can calcuate it at once and reuse
        # So using prefix suffix arrays , shifted/exclusive (can use inclusive as well) :
        # We calculate left and right maxes and then use them to calculate trapped water if the min of left and rightmax is 
        # greater than height[i] 
        # Time : O(n)
        # Space : O(n)
        '''        
        n = len(height)
        ### Exclusive Prefix and Suffix array i.e shifted, for i prefix is leaving i.
        maxprefix = [0]*(n+1)
        for i in range(n):
            maxprefix[i+1] = max(maxprefix[i],height[i])
        print(maxprefix)
            
        maxsuffix= [0]*(n+1)
        for i in range(n-1,-1,-1):
            maxsuffix[i] = max(maxsuffix[i+1],height[i])
        print(maxsuffix)
            
        
        trapped = 0
        for i in range(n):

            if min(maxprefix[i],maxsuffix[i]) > height[i]:
                trapped += min(maxprefix[i],maxsuffix[i]) - height[i]

        return trapped
        '''

        ### Two pointers ###
        # The main equation is min(leftmax,rightmax) - height[i]
        # But till left wall is shorter than any right wall we don't need rightwall for calculation as its minimum
        # of left and right.
        # Similarly if right wall is shorter than any left wall we don't need left walls to calculate.
        # Caveat being in both cases there needs to be a wall.

        L = 1
        R = len(height)-2
        trapped = 0
        leftmax, rightmax = height[0], height[-1]
        
        while L <= R:
            
            print(f'Before processing : lmax:{leftmax} rmax:{rightmax} trapped:{trapped} L:{L} R:{R}')
            if rightmax >= leftmax:
                print('rmax > lmax')
                leftmax = max(height[L], leftmax)
                trapped += leftmax - height[L]
                L += 1
                print(f'trapped:{trapped}')
            else:
                print('rmax < lmax')
                rightmax = max(height[R], rightmax)
                trapped += rightmax - height[R]
                R -= 1
                print(f'trapped:{trapped}')
        return trapped

                


                
        