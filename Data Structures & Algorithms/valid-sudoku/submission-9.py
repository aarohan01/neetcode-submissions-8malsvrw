class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        ### Bitmask ###
        rowmask = [0]*9
        colmask = [0]*9
        squares = [[0]*3 for _ in range(3)]

        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue

                index = int(board[r][c]) - 1

                if rowmask[r] & (1 << index) != 0:
                    return False 
                
                if colmask[c] & (1 << index) != 0:
                    return False 
                
                if squares[r//3][c//3] & (1 << index) != 0:
                    return False

                rowmask[r] |= (1 << index)
                colmask[c] |= (1 << index)
                squares[r//3][c//3] |= (1 << index)

        return True
                
