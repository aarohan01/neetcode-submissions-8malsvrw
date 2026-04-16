class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ### Bruteforce ###
        maxarea = 0
        for i in range(len(heights)):
            maxarea = max(maxarea,heights[i])
            minheight = heights[i]
            for j in range(i+1,len(heights)):

                base = j-i+1 
                minheight = min(minheight,heights[j])
                
                area = base * minheight
                maxarea = max(maxarea,area)
        return maxarea