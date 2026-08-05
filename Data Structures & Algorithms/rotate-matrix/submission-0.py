class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        
        n = len(matrix)
        res = [[0]*n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                res[c][n-1-r] = matrix[r][c]

        for r in range(n):
            for c in range(n):
                matrix[r][c] = res[r][c]

        