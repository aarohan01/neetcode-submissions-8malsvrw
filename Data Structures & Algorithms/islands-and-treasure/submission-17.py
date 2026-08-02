from collections import deque
class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

    ### BFS from all treasure chests, if its landcell then write the level 
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        queue = deque()
        #visit = set()
        INF = 2147483647
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    #visit.add((r,c))
        

        dist = 0
        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()
                #print(grid[r][c])
                if grid[r][c] == INF:
                    #print('here')
                    grid[r][c] = dist


                for dr, dc in directions:
                    nr, nc = r+dr,c+dc
                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] in [-1,0] or grid[nr][nc] != INF:
                        continue

                    queue.append((nr,nc))
                    #visit.add((nr,nc))
        
            dist += 1

        
        


    