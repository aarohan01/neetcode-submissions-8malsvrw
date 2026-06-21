from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        ### Bruteforce - DFS explore all paths multisource ###
        ## From each cell DFS all paths to the nearest treasure
        ## Do it from each cell thus mutlisource
        ## Return aggregation and similar to maxdepth
        # Base case returs inf (failure) or 0 (success)
        # subproblems set the res to min of inf res and sum of 1's in case we hit treasure
        # Thus when treasure not hit we get a huge number (1+INF) but when treasure hits we get (1+0)
        # The 1 is for each recursion level like max depth
        # Time: O(V * 4^V)
        # Space: O(V)  -> visited set and recursion stack
        '''
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        INF = 2147483647

        def dfs(r,c):

            ### Base Cases - Failure ###
            # lower bound min(r,c)
            # Upper bound 
            # water 

            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == -1:
                return INF

            if grid[r][c] == 0:
                return 0

            
            visited.add((r,c))
            res = INF
            for dr, dc in directions:

                ### This is the most important part ###
                # Similar to max depth of binary tree
                # To pass parent for every level we add 1 
                # But we want 1 + ( 1 + ...+ 0 ) when we hit treasure else a higher number 
                # Thus we return INF when base case of false
                res =  min(res, 1 + dfs(r+dr,c+dc))

            visited.remove((r,c))

            return res 
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r,c)
        
        '''


        ### BFS normal coverage multisource/loop from cells ###
        ## Since term nearest and level/distance is important we can go with BFS 
        # BFS is the correct answer
        # BFS from every cell to treasure
        # Mark the cells distance on visits 
        # Idea of BFS - 
        # Need a queue + visited set to mark 
        # We mark visit on enque the source cell
        # Then pop and check if treasure reached if not try all the directions
        # If it has passes the fail case then just continue the loop without adding neighbors
        # After every loop increment level
        # Time: O(V^2)
        # Space: O(V) -> visit set 
        # Cannot mark in the set itself because we need the og grid value while performing next BFS run in for loop
        
        '''
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        INF = 2147483647

        def bfs(r,c):

            queue = deque()
            visited = set()

            ### This is the important part of BFS ###
            # Mark on enque, not when popped/deque 
            queue.append((r,c))
            visited.add((r,c))
            
            level = 0
            while queue:

                for q in range(len(queue)):

                    cr, cc = queue.popleft()
                    
                    ### If treasure is detected ###
                    # Stop and return level #
                    if grid[cr][cc] == 0:
                        return level

                    for dr, dc in directions:
                        nr, nc =  cr+dr, cc+dc
                        if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited or grid[nr][nc] == -1:
                            continue

                        """
                        Instead of this let the treasure be added to queue and check while popping
                        and return level
                        
                        if grid[nr][nc] == 0:
                            return level + 1
                        """
                        
                        queue.append((nr,nc))
                        visited.add((nr,nc))

                        
                level += 1

            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)
        
        '''

        ### BFS normal coverage multisource from treasure - Optimal ###
        ## This is multisource only because there can be multiple treasures
        # Idea - 

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        INF = 2147483647
        visited = set()


        def bfs():

            queue = deque()
            

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 0:
                        queue.append((r,c))
                        visited.add((r,c))

            level = 0 


            while queue:

                for q in range(len(queue)):

                    cr,cc = queue.popleft()

                    if grid[cr][cc] != 0:
                        grid[cr][cc] = min(grid[cr][cc],level)

                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == -1:
                            continue
                    
                        queue.append((nr,nc))
                        visited.add((nr,nc))

                
                level += 1
        
        bfs()
            



        


                        





            
