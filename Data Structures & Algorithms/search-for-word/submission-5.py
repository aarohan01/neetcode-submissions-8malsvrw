from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        


            ### DFS explore all paths i.e. backtracking and return aggregation ###
            ## Why not DFS normal coverage multicell ? 
            ## Because a cell visited need to be available for another path to scan ##
            # SO DFS explore all paths i.e. visited set + backtracking
            # Also the starting cell needs to be the word start so we can do multicell loop 

            ROWS, COLS = len(board), len(board[0])
            directions = [(0,1),(1,0),(-1,0),(0,-1)]


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
                res.append(board[r][c])
    
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if dfs(index+1,nr,nc):
                        return True

                # Undo 
                visited.remove((r,c))
                res.pop()
                
                return False
            
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == word[0]:
                        visited = set()
                        res = []
                        if dfs(0,r,c):
                            return True
            
            return False
                


