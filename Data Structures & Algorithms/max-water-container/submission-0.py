class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ### Bruteforce ###
        areas = []

        for i in range(len(heights)):
            for j in range(len(heights)):

                if i != j:
                    distance = abs(j - i) 
                    height = min(heights[i], heights[j])
                    area =  distance * height
                    print(f'd {distance} * h {height} = {area}')
                    areas.append(area)
        
        print(areas)
        return max(areas)