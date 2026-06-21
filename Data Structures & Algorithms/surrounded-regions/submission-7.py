class Solution:
    def solve(self, board: List[List[str]]) -> None:
        


        ### DFS normal coverage mulitsource ###
        ## Visiting all the nodes only once non-overlapping paths thus normal coverage
        ## No source given, can be disconnected so multisource
        # Idea - 
        # Mark/visit all the 'O' nodes from edge 'O' nodes, careful if using marking instead of set
        # In second pass mark other 'O' nodes 'X' 
        # Time: O(V)
        # Space: O(V) -> recursion stack 


        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        def dfs(r,c):

            ### Base Cases ###
            # min bound 
            # max bound
            # visited 
            # X 
            # Marked ---> important 

            #if min(r,c) < 0 or r == ROWS or c == COLS or board[r][c] == 'X' or board[r][c] == 'M':
                #return 
            #OR
            if min(r,c) < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
                return 


            board[r][c] = 'M'
            print(board)
            for dr, dc in directions:
                dfs(r+dr,c+dc)


        ## Visit the entire board once and mark the edge connected O's and its connected neighbors as 'M'        
        for r in range(ROWS):
            for c in range(COLS):
                if (min(r,c) == 0 or r == ROWS-1 or c == COLS-1) and board[r][c] == 'O':
                    dfs(r,c)


        ## Visit the board once more and mark all emaining 'O' as 'X' and undo marks.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'M':
                    board[r][c] = 'O'
