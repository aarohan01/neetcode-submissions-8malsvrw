class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        ### DFS ###
        ## Specifically given starting location - single source dfs 
        ## Visit only once hence normal coverage
        '''
        ROWS, COLS = len(image), len(image[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        source_color = image[sr][sc]

        def dfs(r,c):

            if min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] == color or image[r][c] != source_color:
                return

            image[r][c] = color

            for dr,dc in directions:
                dfs(r+dr,c+dc)

        
        dfs(sr,sc)
        return image
        '''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image

        m, n = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return

            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image