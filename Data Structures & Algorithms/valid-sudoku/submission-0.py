class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:



        ### Bruteforce ###
        # Given in constraints : rows = 9, cols = 9, board[i][j] = 1-9 or .

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
            
                    
        
                
            




            
        
                
                
            


        