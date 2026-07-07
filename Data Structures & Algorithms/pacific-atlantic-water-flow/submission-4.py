class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        ### Bruteforce ###
        ## DFS explore all paths + multicell
        ## From each cell we perform explore all path and see if we touch atlantic and pacific
        # Time : O(V * 4^V)
        # Space : O(V) -> set, recursion stack.
        '''
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]


        def dfs(r,c,parent):
            
            # Base case : Success 
            # if min bound pacific success
            # if max bound atlantic success
            # Base case : Failure
            # if height is more than the parent cell can't explore further neighbors
            # THAT is why initial parent is float('inf') so first cell always explores neighbors

            nonlocal pacific, atlantic
            if min(r,c) < 0:
                pacific = True
                return 
            
            if r == ROWS or c == COLS:
                atlantic = True
                return

            if heights[r][c] > parent or (r,c) in visited:
                return

            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, heights[r][c])
                if pacific and atlantic:
                    return True
            
            visited.remove((r,c))
            return False

        
        ### Multicell ###
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                pacific, atlantic = False, False
                if dfs(r,c, float('inf')):
                    res.append([r,c])
        
        return res


        '''

        ### DFS normal coverage multicell ###
        ## The idea is row/col 0 cells already flow to pacific
        # row/col m-1,n-1 already flow to atlantic
        # So if we can DFS from these cells and add to sets whereever we can visit
        # Then find common cells we have our answer
        # NOW IMPORTANT PART -> according to question water can flow from higher cell to ocean
        # So when we are visiting from border cell the failure case is if height of that cell is lower
        # we cannot visit. Coz we only visit cells whose are able to flow to current border cell i.e. higher cells
        # Time: O(m*n) -> because of pacific and atlantic sets all cells are visited only once.
        # Space: O(m*n)

        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]


        def dfs(r,c, parentVal, visited):

            # Base Case : Failure
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or heights[r][c] < parentVal:
                return 

            
            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, heights[r][c],visited)
            

        pacific, atlantic = set(), set()
        for r in range(ROWS):
            for c in range(COLS):

                ### Pacific border cells ###
                ## Important : these cells have no real parent value, but in the main dfs we check '<' not 
                # '<=' so the first cell is added and proceeds
                if r == 0 or c == 0:
                    dfs(r, c, heights[r][c], pacific)
                
                ## Not elif because there are cells which satisfy both conditions so those are explored twice

                ### Atlantic border cells ###
                ## Important : these cells have no real parent value, but in the main dfs we check '<' not 
                # '<=' so the first cell is added and proceeds
                if r == ROWS-1 or c == COLS-1:
                    dfs(r, c, heights[r][c], atlantic)

        

        ### Common Cell ###
        res = []
        for cell in atlantic:
            if cell in pacific:
                res.append(list(cell))

        return res




