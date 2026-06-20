class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        ### DFS ###
        ## Specifically given starting location - single source dfs 
        ## Visit only once hence normal coverage
        ## Important edge case - the source color is already color.
        # Neetcode solution handles the edge case by realizing that if the start color is already target 
        # return as is, but this observation is hard to come up.
        # Instead we can just check if the dst cells are also already colored.
        # Time: O(V) 
        # Space: O(V) -> recursion stack
        ROWS, COLS = len(image), len(image[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        source_color = image[sr][sc]

        def dfs(r,c):

            ### Base case 1 - Failure ##
            # min 
            # max 
            # not equal to the source color
            # already marked/visited

            if min(r,c) < 0 or r >= ROWS or c >= COLS or image[r][c] != source_color or image[r][c] == color:
                return

            # Subproblem and recursion
            image[r][c] = color

            for dr,dc in directions:
                dfs(r+dr,c+dc)

        
        dfs(sr,sc)
        return image
        

