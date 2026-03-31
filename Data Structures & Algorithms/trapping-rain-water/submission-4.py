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




                
        