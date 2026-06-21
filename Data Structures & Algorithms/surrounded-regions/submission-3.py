class Solution:
    def solve(self, board: List[List[str]]) -> None:
        


        ### DFS normal coverage mulitsource ###
        ## Visiting all the nodes only once non-overlapping paths thus normal coverage
        ## No source given, can be disconnected so multisource
        # Idea - 
        # Mark/visit all the 'O' nodes from edge 'O' nodes, careful if using marking instead of set
        # In second pass mark other 'O' nodes 'X' 


        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        def dfs(r,c):

            ### Base Cases ###
            # min bound 
            # max bound
            # visited 
            # X

            if min(r,c) < 0 or r == ROWS or c == COLS or board[r][c] == 'X' or board[r][c] == 'M':
                return 


            board[r][c] = 'M'
            print(board)
            for dr, dc in directions:
                dfs(r+dr,c+dc)

        
        for r in range(ROWS):
            for c in range(COLS):
                if min(r,c) == 0 or r == ROWS-1 or c == COLS-1 and board[r][c] == 'O':
                    dfs(r,c)

        #print(board)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'M':
                    board[r][c] = 'O'
