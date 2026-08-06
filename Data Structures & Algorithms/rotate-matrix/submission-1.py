class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        '''
        n = len(matrix)
        res = [[0]*n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                res[c][n-1-r] = matrix[r][c]

        for r in range(n):
            for c in range(n):
                matrix[r][c] = res[r][c]
        '''

        '''
        n = len(matrix)
        res = [[0]*n for _ in range(n)]
        
        for i in range(4):
            for r in range(n):
                for c in range(n):
                    matrix[c][n-1-r] = matrix[r][c]
        '''

        ### Layer by layer left to right ###
        # if size is n then n-1 rotatons
        # first shift the outer layer form left to right then reduce top,bottom, l,r
        # repeat until l < r
        n = len(matrix)
        top, bottom = 0,n-1
        l, r = 0, n-1
        # since its derived (i,j) is (j,n-1-i)
        ### Just Imagine - when the top layer item moves the row stays stable at top and col moves with i
        # similarly right layer row moves with i and col stays stable at r
        # siminarly.....
        ## 

        while l < r:
            for i in range(l,r):
                
                ### Just for reference ###
                '''
                topleft = matrix[top][i] 
                topright = matrix[top][n-1-i] 
                bottomright = matrix[bottom][n-1-i] 
                bottomleft = matrix[bottom][i]
                '''

                temp = matrix[top][i]

                matrix[top][i] = matrix[n - 1 - i][l]
                matrix[n - 1 - i][l] = matrix[bottom][n - 1 - i]
                matrix[bottom][n - 1 - i] = matrix[i][r]
                matrix[i][r] = temp

                
            
            top += 1
            bottom -= 1
            l += 1
            r -= 1
        




