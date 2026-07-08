import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        


        ### Dijkstra ###
        ## After observing the example, we need to do bfs but pick only lowest cost neighbor to explore everytime
        # Also, wrong assumtion is only 1 grid at a time, right assumption is path is clear if the max level equals time
        # So we just have to store the max number in this shortest path.


        ## Dijkstra ##
        # BFS with priority queue + visited (instead of res dict cos storing all values is unnecssary)
        # No mark on enque, pop only the lowest
        # maintain max
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1), (-1,0),(0,-1)]

        minheap = []
        heapq.heappush(minheap, (0,(0,0)))

        visited = set()
        maxt = grid[0][0]

        while minheap:

            cost,(r,c) = heapq.heappop(minheap)

            if (r,c) in visited:
                continue

            visited.add((r,c))
            maxt = max(maxt, grid[r][c])

            if (r,c) == (ROWS-1,COLS-1):
                return maxt

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited:
                    continue

                heapq.heappush(minheap,(grid[nr][nc],(nr,nc)))

        
        return -1
    

