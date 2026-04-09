class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        ROWS, COLS = len(matrix), len(matrix[0])
        # Create prefix matrix with extra row and column
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for r in range(ROWS):
            for c in range(COLS):
                self.prefix[r+1][c+1] = (matrix[r][c] + 
                                        self.prefix[r][c+1] + 
                                        self.prefix[r+1][c] - 
                                        self.prefix[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # All indices are shifted by +1 due to our extra row/column
        return (self.prefix[row2+1][col2+1] - 
                self.prefix[row1][col2+1] - 
                self.prefix[row2+1][col1] + 
                self.prefix[row1][col1])

### Without shifting and using extra row/column ###
'''
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
'''