from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        minutes = 0


        ### Multisource ###
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        

        ### Edge ###
        if not fresh:
            return 0

        
        while queue:

            for _ in range(len(queue)):
                
                print(queue)
                r,c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue

                    queue.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            minutes += 1
            if fresh == 0:
                return minutes

        return -1
                
