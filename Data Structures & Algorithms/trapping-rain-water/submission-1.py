class Solution:
    def trap(self, height: List[int]) -> int:


        ### Bruteforce ###
        # For each element i find the the tallest on left and right side higher than itself
        # the area over it is min of those height - height of i
        trapped = 0
        for i in range(1,len(height)-1):

            leftmax = max(height[:i])
            rightmax = max(height[i+1:])

            if min(leftmax,rightmax) > height[i]:
                trapped += min(leftmax,rightmax) - height[i]
            
            print(f'i:{i} l:{leftmax} r:{rightmax} t:{trapped}')

        return trapped






                
        