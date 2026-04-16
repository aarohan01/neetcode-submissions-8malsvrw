class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ### Bruteforce ###
        # Loop for each i, maxarea is either height of i or the minheight from i till each j*distace
        # Time: O(n^2)
        # Space: O(1)
        '''
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
        '''

        ### Stack optimized ###
        # Case 1: current is lower or equal than previous -> keep popping and calculate area
        # Case 2: current is higher  -> add to stack 
        # Case final: cases than reach final length --> IMP : 
        # The final remaining heights are in increasing order and are the ones that can be 
        # extended till the end from their valid index
        # Thus we don't need any other or current index for them 
        # The width of the histogram - the valid index is their width

        stack = []
        maxarea = 0

        for i in range(len(heights)):
            
            # Case 2
            if not stack or heights[i] > stack[-1][1]:
                
                # Pait -> tuple of valid index, hight, own index
                pair = (i,heights[i])
                stack.append(pair)
                #print(stack)

            else:
                # Case 1:
                    while stack and heights[i] <= stack[-1][1]:

                        valid_idx, valid_h = stack.pop()
                        area = (i-valid_idx)*valid_h
                        maxarea = max(maxarea, area)
                        #print(stack, maxarea)

                    pair = (valid_idx, heights[i])
                    stack.append(pair)
            
        #print(stack, maxarea)

        # Case final : IMP -> These extend till the end so we don't need current index
        # All of them have width equal to lenght of the histogram starting from valid index
        tlen = len(heights)
        while stack:
            valid_idx, valid_h = stack.pop()
            area = (tlen - valid_idx)  *valid_h
            maxarea = max(maxarea, area)
            #print(stack, maxarea)

        return maxarea

