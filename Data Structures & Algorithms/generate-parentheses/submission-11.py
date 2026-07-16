class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        ### Bruteforce - recursion ###
        # This solution is simple
        # Start with an empty array and keep selecting either open or close bracket
        # if length of pattern hits n*2 do a check for validity and add to result if valid
        # Time: O(2^2n * 2n) -> nary tree here binary, max height is 2n, O(2n) for copying
        # Space: O(n^2) aux O(n^2) + O(n), n^2 is for holing all elements in during one path as each level
        # of recusion in a path will hold max 2n so a path will hold 1+2+...2n 
        # O(n) for recursion stack
        '''
        res = []
        def checker(patternN):
            count = 0

            for bracket in patternN:
                if bracket == '(':
                    count += 1
                else:
                    count -= 1

                if count < 0:
                    return False

            return count == 0


        def generate(pattern):

            if len(pattern) == n*2:
                if checker(pattern):
                    res.append(''.join(pattern))
                return

            
            generate(pattern + ['('])
            generate(pattern + [')'])


        generate([])
        return res
        '''

            

        ### Backtracking -- Combine the check and pattern  ###
        # Instead of seperate pattern array, a global pattern array can be used and popped
        # Similarly the check can happen implicitly 
        # Time: O(n * 4^n) -> Loose bound O(2^2n) i.e. O(4^n) from the dfs nary tree (binary) and 2n height, n for copying.
        # Space: O(n) -> O(2n) aux space because of the recursion stack and temp pattern storage
        # Space: O(n*4^n) output space i.e 2^2n pairs patterns of max size n. This is loose bound 
        # Why loose bound -> since in reality we are not exploring all the branches.

        res, pattern = [], []
        def dfs(openN, closeN):

            if openN == closeN == n:
                res.append(''.join(pattern))
                return

            if openN < n:
                pattern.append("(")
                dfs(openN+1, closeN)
                pattern.pop()

            ### The most important condition is this ###
            ## if we do closeN < n, the backtracking will allow starting with ')'
            # At the root of backtracking tree openN and closeN is 0 so after executing openN loop 
            # closeN loop will be executed with OpenN, closeN as 0
            # Thus closeN should only execute when its lower than openN so that it atmost becomes equal
            if closeN < openN:
                pattern.append(")")
                dfs(openN, closeN+1)
                pattern.pop()

        dfs(0,0)
        return res

                







