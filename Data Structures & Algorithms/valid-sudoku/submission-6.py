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
        '''
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
        '''

        ### Bitmask solution ###

        # Nine rows, each 0 integer represents 9 binary flags for nine possible decimal numbers fro, 1 to 9
        # If 1 is present in row 1 then row[1]'s 0th flag is set to 1, for val 2 row[1]'s 1st flag is set to 1
        rows = [0]*9

        # Nine cols 
        cols = [0]*9

        # Nine squares
        squares = [[0]*3 for _ in range(3)]
        


        for r in range(9):
            for c in range(9):
                

                if board[r][c] == '.':
                    continue
                
                # String to integer
                val = int(board[r][c])

                ### Check val's flag set in rows, col and squares ###
                ## To check we shift 1 by val and & it with current value of that row, col, square
                # Ex : if val is 2 then in rows, col, square if 1st bit is set we & and get 1 its seen if we get 0 its not seen

                # IMP : val - 1 because for val 1 index 0 bit flag
                index = val - 1
                bitval = 1 << index

                # Check if seen by &
                if bitval & rows[r]:
                    return False
                
                if bitval & cols[c]:
                    return False 
                
                if bitval & squares[(r//3)][(c//3)]:
                    return False 

                # If not seen set the flags by OR for each row
                # Why OR -> every row index represent all digit flags
                # For example : row[0] = 000000011 that means in row[0] values 1 and 2 were seen 
                # Now if new value seen is 3 we OR it with the bit val to get 000000111

                rows[r] |= bitval      # rows[r] = rows[r] | bitval
                cols[c] |= bitval
                squares[(r//3)][(c//3)] |= bitval   
                              

        return True



                    
        
                
            




            
        
                
                
            


        