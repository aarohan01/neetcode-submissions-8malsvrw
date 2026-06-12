class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        ### Bruteforce - Backtracking as subsets no dupes ###
        # Generating all subsets but selecting only with size k
        # No reuse, no dupes so subset normal pattern
        # Time: O(k * 2^n)
        # Space: O(k) -> at a time only k elements stored
        '''
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
        '''

        ### Backtracking combination normal ###
        # Instead of doing full subsets we can use the combination formula pattern of for-loop ahead recursion
        # No repetition, no dupes, order does not matter and select k from n -> combination normal pattern
        # Start with a index and for loop ahead indexes (advance) recurse with base case of len(combination) and i >n
        # do it for all number till n
        
        res, combination = [], []

        def dfs(i):

            # Base Case 1 - Success 
            if len(combination) == k:
                res.append(combination.copy())
                return 
            
            # Base Case 2 - Failure
            if i > n or len(combination) > k:
                return 

            # Loop choices and then choices ahead
            for start in range(i,n+1):
                
                
                combination.append(start)
                dfs(start+1)
                combination.pop()
        

        dfs(1)
        return res
        