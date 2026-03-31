from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        ### Solution ###
        # Since GRID & minimum == BFS
        # In normal BFS we start from (0,0), but here we want start from rotting fruits at start 
        # 1. But there can be multiple rotting fruits. Thus go through the matrix and add all rotting fruits in queue and visited.
        # In normal BFS we process the neigbors of only the poppped node from matrix and level up,
        # 1. But here we want to process the entire queue first and then level up. 
        # 2. This also means len(queue) cannot be loop ending, what is the end -> no fresh fruits 
        # 3. So count the number ahead and reduce it after processing a neighbor from fresh to rotting.
        #
        # We can also mark the visited neighbor as rotten changing it to 2 instead of maintaining a set of visited.
        # Both versions work. Here since we rot every fruit the changing to 2 is more preferable method.



        # Setup 
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        #visited =  set()
        fresh = 0
        minutes = 0

        # Rotting and Fresh
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    #visited.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        print(f'Rotten: {queue} Fresh: {fresh} Time: {minutes}')
        
        # Loop till no fresh fruits left.
        while fresh > 0:
            pfresh = fresh
            qlen = len(queue)
            # While the queue has any rotten fruit
            while qlen > 0:

                # For each rotten we pop and check the neigbors and rot them
                r, c =  queue.popleft()

                # Neighbors check conditions:
                # 1. min bound 
                # 2. max bound 
                # 3. blocked
                # 4. already visited

                directions = [[0,1],[1,0],[0,-1],[-1,0]]
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc

                    #if min(nr,nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] in [0,2] or (nr,nc) in visited:
                    if min(nr,nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] in [0,2]:
                        continue 
                    
                    print(f'Appending : {(nr,nc)}')
                    queue.append((nr,nc))
                    #visited.add((nr,nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            
                qlen -= 1

            # Edge case where no nighbor is fresh             
            if pfresh == fresh:
                return -1

            print(f'\n')
            minutes += 1


        return minutes
        