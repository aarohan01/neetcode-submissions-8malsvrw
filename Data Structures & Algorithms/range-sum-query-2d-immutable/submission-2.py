class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        ### Prefixsum of Matrix -
        self.matrix =  matrix
        print(matrix)
        ROWS, COLS = len(self.matrix), len(self.matrix[0])

        for r in range(ROWS):
            for c in range(COLS):

                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    self.matrix[r][c] = self.matrix[r][c] + self.matrix[r][c-1]
                elif c == 0:
                    self.matrix[r][c] =  self.matrix[r][c] + self.matrix[r-1][c]
                else:
                    self.matrix[r][c] = self.matrix[r][c] + ((self.matrix[r][c-1] + self.matrix[r-1][c]) - self.matrix[r-1][c-1]) 
        
        print(f'After:{self.matrix}')


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.matrix[row1-1][col2] if row1 > 0 else 0
        left = self.matrix[row2][col1-1] if col1 > 0 else 0
        top_left = self.matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return self.matrix[row2][col2] - (top + left - top_left)