class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ### Backtracking - Constrainded Condition ###
        # For every row we try to place a queen in a column based on few conditions.
        # Conditions: If a queen is placed somewhere then
        # 1.No queen should be in same row (this is auto satisfied since we are only trying one row at a time)
        # 2.No queen should be in same column (as the previous queen) - check set
        # 3.No queen should be in positive diagonal - each forward & down diagonal can be identified by (r+c) - check set
        # 4.No queen should be in negative diagonal - each backward & down diagonal can be identified by (r-c) - check set
        # NOTE - diagonals are important the entire diagonal can be identified by r+c and r-c not just the next cell in the diagonal
        # Based on it we make a choice and then try choosing for next row if doesn't work we undo choice
        # Time: O(n!) -> nary tree max height of n could be n^n but here every next choice is (n-1) not even considering 
        # the diagonal, so O(n!)
        # Space: (n^2) aux -> recursion stack O(n) + at a time one entire board is stored O(n^2) in a path
        
        ## Note the difference between explore all paths and this type (backtracking writing style) is that 
        # the choice is dependent on the for loop thus make and undo it in the loop
        # explore all paths can also be written this way but we do it diffenently we keep it as base case and visit outside
        # the loop thus undo outside.

        ROWS, COLS = n, n
        col_marked = set()  # c
        pdiag_marked = set() # (r+c)
        ndiag_marked = set()  # (r-c) 
        board = [['.']*COLS for _ in range(ROWS)]

        res = []
        def dfs(r):

            if r == ROWS:
                copy = [ ''.join(row) for row in board ]
                print(copy)
                res.append(copy)
                return 

            for c in range(COLS):

                if c not in col_marked and (r+c) not in pdiag_marked and (r-c) not in ndiag_marked:
                    
                    # Choice
                    board[r][c] = 'Q'
                    col_marked.add(c)
                    pdiag_marked.add((r+c))
                    ndiag_marked.add((r-c))
                    
                    # Recurse
                    ### Index is row, for every row we are trying a column to place queen in based on conditions
                    # Then move ahead.
                    dfs(r+1)
                    
                    # Undo choice
                    board[r][c] = '.'
                    col_marked.remove(c)
                    pdiag_marked.remove((r+c))
                    ndiag_marked.remove((r-c))
        
        dfs(0)
        return res



            