from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        ### BFS normal coverage single source ###
        ## All nodes need to be visited once so normal coverage 
        ## Only form a given single source, no disconnection - single source
        # Idea :
        # Visit Set + Queue create
        # Mark on enque the first cell i.e. source 
        # While queue exists, loop the queue -> For looping range of queue is to only loop the old neighbors 
        # so when new neigbors of the popped node are added they aren't processesed without incrementing level
        # So all the elements present originally have same level/distance.
        # Pop a node from left.
        # Process and check --> If any breaking condition 
        # Then loop the neighbors if valid mark and enque
        # Increment level
        # If queue is empty return default answer
        # Time: O(V) or O(m*n)
        # Space: O(V) or O(m*n) -> visit set + queue
        ## Can use marking instead of visit set in this question since no need for old value and just binary

        
        # Setup 
        ROWS, COLS = len(grid), len(grid[0])
        queue  = deque()
        visited = set()

        # Need to check if the first node itself is valid
        if grid[0][0] == 1:
            return -1

        ### Mark and enque source node ###
        queue.append((0,0))
        visited.add((0,0))
        length = 0

        #print(f'Lenght: {length} Visited : {(0,0)}')

        # Loop through the queue 
        while queue:
            
            ### Maintain Level ###
            for i in range(len(queue)):

                # pop the node in the queue 
                r, c = queue.popleft()

                # Check if matrix bounds reached, notice AND 
                # THIS IS THE IMPORTANT BREAKING CONDITION IF ANY PATH IS FOUND WE RETURN 
                if r == ROWS-1 and c == COLS-1:
                    return length 

                # Loop through neighbors and check which is correct to add
                directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]

                for dr, dc in directions:

                    # Check which goes through without violating base conditions
                    # If some neighbour doesn't just continue the loop to check next neighbor

                    # 1. min bounds 
                    # 2. max bound on row or col
                    # 3. blocked
                    # 4. already visited
                    nr, nc = r + dr, c + dc 
                    if  min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue 

                    ### Mark and enque neighbors ###
                    queue.append((nr, nc))
                    visited.add((nr, nc))

            # Increment Level
            length += 1
            #print(f'Lenght: {length} Visited : {queue}')

        ## IF PATH NOT FOUND
        return -1


            


