from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        ### Solution ###
        # Use a queue and set to maintain what to explore and what is already visited

        
        # Setup 
        ROWS, COLS = len(grid), len(grid[0])
        queue  = deque()
        visited = set()

        # Need to check if the first node itself is valid
        if grid[0][0] == 1:
            return -1

        # Add the first node and set level to 0
        queue.append((0,0))
        visited.add((0,0))
        length = 0
        print(f'Lenght: {length} Visited : {(0,0)}')

        # Loop through the queue 
        while len(queue) > 0:
            for i in range(len(queue)):     
                # pop the node in the queue 
                r, c = queue.popleft()

                # Check if matrix bounds reached, notice AND
                if r == ROWS-1 and c == COLS-1:
                    return length 

                # Loop through neighbors and check which is correct to add
                directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]

                for dr, dc in directions:

                    # Check which goes through without violating base conditions
                    # If some neighbour doesn't just continue the loop to check next neighbor

                    # 1. min bounds 
                    # 2. max bound on row or col
                    # 2. blocked
                    # 3. already visited
                    nr, nc = r + dr, c + dc 
                    if  min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue 

                    queue.append((nr, nc))
                    visited.add((nr, nc))

            length += 1
            print(f'Lenght: {length} Visited : {queue}')

        return -1


            


