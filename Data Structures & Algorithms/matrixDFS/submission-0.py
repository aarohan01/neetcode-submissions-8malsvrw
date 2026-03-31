class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        r,c = 0,0
        visit =  set()

        def dfs(grid,r,c,visit):
            #nonlocal r, c, visit
            ROWS, COLS = len(grid), len(grid[0])

            ### Base cases:
            ## Case 1 : Failure
            # 1. r or c goes below 0
            # 2. r or c reaches ROWS/COLS
            # 3. grid value is 1
            # 4. Already visited
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1 or (r,c) in visit:
                return 0
            
            ## Case 2 : Success 
            # Hits bottom 
            if r == ROWS-1 and c == COLS-1:
                return 1

            # Visit the node
            visit.add((r,c))
            print((r,c))

            # Maintain count from each node
            count = 0

            # Explore neighbors 
            count += dfs(grid, r+1, c, visit)
            count += dfs(grid, r-1, c, visit)
            count += dfs(grid, r, c+1, visit)
            count += dfs(grid, r, c-1, visit)

            # Reaches bottom
            # Backpropogate node removal from the visit, so next path doesn't hit visit base case 
            print(count)
            visit.remove((r,c))
            return count


        

        return dfs(grid, r, c, visit)
        