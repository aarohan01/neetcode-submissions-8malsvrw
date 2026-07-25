from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        '''
            ### DFS explore all paths i.e. backtracking and return aggregation ###
            ## Why not DFS normal coverage multicell ? 
            ## Because a cell visited need to be available for another path to scan ##
            # SO DFS explore all paths i.e. visited set + backtracking + return prapogation
            # Also the starting cell needs to be the word start so we can do multicell loop 
            ## Backtracking keep success case ahead since no relation to bounds check.##
            # Time: O(m*n * 4^L) -> O(4^L) for the DFS 4 directions and L depth of nary tree where 
            # L is lenght of the word  and m*n nodes in grid (multicell)
            # Space: O(L) aux -> recursion stack + visited set

            ROWS, COLS = len(board), len(board[0])
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            visited = set()  ### Since its popped its okay to be commmon same for res
            #res = []

            def dfs(index, r,c):
                #print(res, index)

                ### Base Case : Success 
                if index == len(word):
                    return True

                ### Base Case : Failure
                if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] != word[index]:
                    return False

                # Choice / Subproblem
                visited.add((r,c))
                #res.append(board[r][c])
    
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if dfs(index+1,nr,nc):
                        return True

                # Undo 
                visited.remove((r,c))
                #res.pop()
                
                return False
            

            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == word[0]:
                        if dfs(0,r,c):
                            return True
            
            return False

        '''

        ### Little bit more optimization ###
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS, COLS = len(board), len(board[0])
        #visited = set()

        def dfs(index,r,c):
            
            if index >= len(word):
                return True
            #if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] != word[index]:
                #return False
            if min(r,c) < 0 or r == ROWS or c == COLS or board[r][c] == '#' or board[r][c] != word[index]:
                return False
    
            
            #visited.add((r,c))
            temp = board[r][c]
            board[r][c] = '#'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                if (nr,nc) != (r,c):
                    if dfs(index+1,nr,nc):
                        return True
            #visited.remove((r,c))
            board[r][c] = temp

            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(0,r,c):
                        return True
        return False

                


