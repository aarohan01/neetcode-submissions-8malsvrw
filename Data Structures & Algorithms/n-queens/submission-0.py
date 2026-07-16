class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

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
                    dfs(r+1)
                    
                    # Undo choice
                    board[r][c] = '.'
                    col_marked.remove(c)
                    pdiag_marked.remove((r+c))
                    ndiag_marked.remove((r-c))
        
        dfs(0)
        return res



            