class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        ### Solution ###
        ## After seeing the solution ##
        # Since rows are sorted and 1st term is the lowest and log time complexity we can use this to our adv
        # Matrix by default will have equal number of cols in each row
        # Need to first binary search on the rows to find a candidate row : logm
        # Run binary search on the candidate row : logn

        # Algo :
        # Search the row by - two pointers for rows, calculate mid row (same as binary search) 
        # -- if the target is greater than greatest element of mid row then change the top 
        # -- else if the bottom is lesser than smallest element of mid row then change the bot
        # -- else the row is found so break (there is a caveat/edge case)
        # Case where the target is not in the ranges of the rows ex row1 [1,2,3] [5,6,7] target = 4
        # -- return False 
        # Run binary search on the candidate row 

        ROWS = len(matrix)
        COLS = len(matrix[0]) 

        # Search the candidate row
        top = 0
        bot = ROWS - 1

        while top <= bot :
            crow  =  (top + bot)//2

            if target > matrix[crow][-1]:
                top = crow + 1
            elif target < matrix[crow][0]:
                bot = crow - 1
            else : 
                break
        
        # Caveat / Edge case - not in ranges -   top greater than bot 
        if top > bot :
            return False 
        
        # Binary search 
        l =  0
        r = COLS - 1

        while l <= r :
            
            m = (l+r)//2
            if target > matrix[crow][m]:
                l = m + 1
            elif target < matrix[crow][m]:
                r = m - 1
            elif target == matrix[crow][m]:
                return True
        return False

        