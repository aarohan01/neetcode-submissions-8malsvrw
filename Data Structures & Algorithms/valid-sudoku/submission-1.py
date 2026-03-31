class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:



        ### Solution 1 ###
        # Given in constraints : rows = 9, cols = 9, board[i][j] = 1-9 or .
        # Check for rows, then cols and then squares presence of duplicates
        # Time : O(n^2)
        # Space : o(n) - at a time only n elements in seen when grid is n*n
        '''
        ROWS, COLS = 9, 9

        # Check rows
        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                
                if board[r][c] == '.' :
                    continue 
                if board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])

        
        # Check cols
        for c in range(COLS):
            seen = set()
            for r in range(ROWS):
                if board[r][c] == '.' :
                    continue 
                if board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])
 
        
        # Check internal 
        for r in range(0,ROWS,3):
            for c in range(0,COLS,3):
                br = (r//3)*3
                bc = (c//3)*3
                print(f'{br}-{bc}')

                seen = set()
                for i in range(br, br+3):
                    for j in range(bc, bc+3):
                        
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in seen:
                            return False 
                        else:
                            seen.add(board[i][j])


        return True
        '''

        ### Solution 2 ### More complexity but easier code
        # Checking rows, cols and grids at once 
        # We can use hashmap of hashsets to determine at once 
        # rows are indexed by 0 to 9 
        # cols are indexed by 0 to 9 
        # Internal squares can be indexed by r//3 , c//3 as we id each internal square by 0-3,0-3


        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        squares = {}
        for i in range(3):
            for j in range(3):
                squares[(i,j)] = set()

        

        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue 
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3),(c//3)]):
                    return False    
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])

        return True



                    
        
                
            




            
        
                
                
            


        