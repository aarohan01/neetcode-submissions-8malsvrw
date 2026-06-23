class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ### Solution ###
        ## Need to visit each cell only once normal coverage
        ## Source given and only one cell, no disconnection so single source BFS
        # Exactly same BFS only differece is path == vertices visited, hence length starts at 1 and 
        # diagonal inclued in directions.
        # Time: O(v) or here since square matrix O(m*n) becomes O(n^2)
        # Space: O(V) -> visited set + queue
        ## Since in this question 

        # Setup 
        ROWS, COLS = len(grid), len(grid[0])
        queue  = deque()
        visited = set()

        # Need to check if the first node itself is valid
        if grid[0][0] == 1:
            return -1

        # Add the first node and set level to 0
        ### Important - Mark on enque ###
        queue.append((0,0))
        #visited.add((0,0))
        grid[0][0] = 1
        length = 1
        #print(f'Lenght: {length} Visited : {(0,0)}')

        # Loop through the queue 
        while queue:
            for i in range(len(queue)):     
                # pop the node in the queue 
                r, c = queue.popleft()

                # Check if matrix bounds reached, notice AND 
                # THIS IS THE IMPORTANT BREAKING CONDITION IF ANY PATH IS FOUND WE RETURN 
                if r == ROWS-1 and c == COLS-1:
                    return length 

                # Loop through neighbors and check which is correct to add
                directions = [ [1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1] ]

                for dr, dc in directions:

                    # Check which goes through without violating base conditions
                    # If some neighbour doesn't just continue the loop to check next neighbor

                    # 1. min bounds 
                    # 2. max bound on row or col
                    # 3. blocked
                    # 4. already visited
                    nr, nc = r + dr, c + dc 
                    #if  min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visited:
                    #    continue 
                    if  min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1:
                        continue 


                    ### Important - Mark on enque ###
                    queue.append((nr, nc))
                    #visited.add((nr, nc))
                    grid[nr][nc] = 1

            # Next in queue
            length += 1
            print(f'Lenght: {length} Visited : {queue}')

        ## IF PATH NOT FOUND
        return -1