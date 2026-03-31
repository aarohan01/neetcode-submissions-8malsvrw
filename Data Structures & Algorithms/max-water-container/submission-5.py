class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ### Bruteforce ###
        # Calculate all the areas and replace the maxarea. Return the final answer
        # Time : O(n^2)
        # Space : O(1)
        '''
        maxarea = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                
                distance = j - i
                height = min(heights[i], heights[j])
                area =  distance * height
                
                print(f'd {distance} * h {height} = {area}')
                maxarea = max(maxarea, area)
        
        print(maxarea)
        return maxarea
        '''

        L = 0
        R = len(heights) - 1

        maxarea = 0

        while L < R:
            
            distance = R - L
            height = min(heights[L], heights[R])
            area =  distance * height

            print(f'{L}-{R}')    
            print(f'd {distance} * h {height} = {area}')
            
            maxarea = max(area, maxarea)

            if heights[L] <= heights[R]:
                L += 1
            elif heights[L] > heights[R]:
                R -= 1

        return maxarea
