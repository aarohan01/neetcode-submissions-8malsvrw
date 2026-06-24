from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        ### BFS normal coverage multisource ###
        ## Visiting all the nodes only once non-overlapping paths thus normal coverage
        ## Multiple source given, so multisource
        # The one additional condition is regarding fresh and rotten fruit
        # We don't necessarily have to explore all levels, if no fresh fruit then return minutes immediately.
        # So it can also be 0 or >0
        # If fresh cannot be reached return -1


        ### Setup ###
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        ### Multisource ###
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1


        ### While the queue has any rotten fruit ###
        while fresh and queue:
                

                for _ in range(len(queue)):

                    # For each rotten we pop and check the neigbors and rot them
                    r, c =  queue.popleft()

                    # Neighbors check conditions:
                    # 1. min bound 
                    # 2. max bound 
                    # 3. blocked i.e. either 0 or 2.
                    for dr,dc in directions:
                        nr, nc = r+dr, c+dc

                        if min(nr,nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] in [0,2]:
                            continue 
                    
                        print(f'Appending : {(nr,nc)}')
                        queue.append((nr,nc))
        
                        grid[nr][nc] = 2
                        fresh -= 1
                
                minutes += 1
                ## Exits the loop if fresh has reached zero ###
                ## This is the breaking condition ##

        ## Return 0 if no fresh at the start
        ## Return minutes i.e. > 0 if fresh becomes 0
        ## Return -1 if fresh != 0 but queue is not empty
        return minutes if fresh == 0 else -1