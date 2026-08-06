class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        ### DFS starting from (0,0) keep moving right 
        # when hit base case change direction 
        # keep changing directions 

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        ROWS, COLS = len(matrix), len(matrix[0])
        d = 0
        res = []
        def dfs(r,c):
            nonlocal d
            if min(r,c) < 0 or r == ROWS or c == COLS or matrix[r][c] =='#':
                return False


            res.append(matrix[r][c])
            matrix[r][c] = '#'

            dr, dc = directions[d]
            nr, nc = r+dr, c+dc
            if not dfs(nr,nc):
                d = (d+1)%4
                dr, dc = directions[d]
                nr, nc = r+dr, c+dc
                dfs(nr,nc)
                
            
        dfs(0,0)
        return res

        