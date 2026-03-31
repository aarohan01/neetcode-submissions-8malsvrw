class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ### BruteForce ###
        
        # Check rows
        for r in range(9):
            rows = set()
            for c in range(9): 
                
                if board[r][c] in rows and board[r][c] != '.':
                    print('1')
                    return False
                rows.add(board[r][c])

        
        # check columns 
        for c in range(9):
            cols = set()
            for r in range(9):
                if board[r][c] in cols and board[r][c] != '.':
                    print('2')
                    return False
                cols.add(board[r][c])

        # check the squares 
        for r in range(0,9,3):
            for c in range(0,9,3):

                br = (r // 3)*3 
                bc = (c // 3)*3
                squares = set()
                print(f'loop -{r}-{c}')
                for i in range(br, br+3):
                    for j in range(bc, bc+3):
                        print(f'{i}-{j}')
                        if board[i][j] in squares and board[i][j] != '.':
                            print('3')
                            return False
                        squares.add(board[i][j])
                print(squares)
        return True