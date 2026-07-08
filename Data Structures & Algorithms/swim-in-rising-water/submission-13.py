import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        


        ### Prim's i.e. Dijkstra but with visited set and local cost alone ###
        ## After observing the example, we need to do bfs but pick only lowest cost neighbor to explore everytime
        # Also, wrong assumtion is only 1 grid at a time, right assumption is path is clear if the max level equals time
        # So we just have to store the max number in this shortest path.


        ## Dijkstra ##
        # BFS with priority queue + visited (instead of res dict cos storing all values is unnecssary)
        # No mark on enque, pop only the lowest
        # maintain max
        '''
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1), (-1,0),(0,-1)]
        
        # Heap : (cost,r,c)
        minheap = []
        heapq.heappush(minheap, (0,0,0))
        
        # Visit set, no mark on enque
        visited = set()
        
        # Max value discoverd during path
        maxt = grid[0][0]

        while minheap:

            cost,r,c = heapq.heappop(minheap)
            
            # Don't visit if alredy visited
            if (r,c) in visited:
                continue

            # Visit
            visited.add((r,c))
            maxt = max(maxt, grid[r][c])

            # Breaking Condition
            if (r,c) == (ROWS-1,COLS-1):
                return maxt

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited:
                    continue

                heapq.heappush(minheap,(grid[nr][nc], nr, nc))

        
        return -1
        '''


        ### Dijkstra OR Bottleneck/MinMax Dijkstra ###
        # Instead of Prim's we can use dijkstra i.e. it will be called minmax/bottleneck dijkstra if we maintain
        # state in the heap itself. Both are optimal and exactly same bu the maintenance of max in heap i.e. cost from source 
        # is thus called dijkstra
  
        # BFS with priority queue + visited (instead of res dict cos storing all values is unnecssary)
        # No mark on enque, pop only the lowest
        # maintain max in heap itself
        # Time: O(E*logV) OR VlogV since E == V here the entire path
        # Also can say n^2logn because max E/V can be n^2 -> n^2logn^2 -> 2n^2longn -> n^2logn (square matrix)
        # Space: O(V) -> visited set thus O(n^2)

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1), (-1,0),(0,-1)]
        
        # Heap : (maxcost,r,c)
        minheap = []
        heapq.heappush(minheap, (grid[0][0],0,0))
        
        # Visit set, no mark on enque
        visited = set()
        

        while minheap:

            maxcost,r,c = heapq.heappop(minheap)
            
            # Don't visit if alredy visited
            if (r,c) in visited:
                continue

            # Visit
            visited.add((r,c))

            # Breaking Condition
            if (r,c) == (ROWS-1,COLS-1):
                return maxcost

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited:
                    continue

                # NOTE Here not addition but OR, so max from source till current
                heapq.heappush(minheap,(max(grid[nr][nc], maxcost), nr, nc))

        
        return -1
    

