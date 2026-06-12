class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        ### Bruteforce - Backtracking as subsets no dupes ###
        # Generating all subsets but selecting only with size k
        # No reuse, no dupes so subset normal pattern
        # Time: O(k * 2^n)
        # Space: O(k) -> at a time only 

        res, combination = [], []

        def dfs(i):

            # Base case 1 :  success 
            if len(combination) == k:
                res.append(combination.copy())
                return 

            # Base case 2 : failure
            if i > n or len(combination) > k:
                return 
            
            # Choice 1:
            # Take and advance
            combination.append(i)
            dfs(i+1)

            # Choice 2:
            # Skip and advance
            combination.pop()
            dfs(i+1)
        
        dfs(1)
        return res


        