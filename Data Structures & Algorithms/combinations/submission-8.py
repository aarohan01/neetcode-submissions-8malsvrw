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
            # len(combination) > k not needed coz k always hits unlike sum
            if i > n:
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
        # Time: O(k * nCk) 
        # Space: o(k)

        res, combination = [], []

        def dfs(i):

            # Base Case 1 - Success 
            if len(combination) == k:
                res.append(combination.copy())
                return 
            
            # Base Case 2 - Failure
            if i > n:
                return 

            # Loop choices and then choices ahead
            # Select a number and recurse its combinations with numbers ahead it
            # Then next number and its combinations with numbers ahead it 
            # Ahead it coz if we do for first number again it will have dupes in the result
            # basically take and advances continuous with the same start number then remove that number
            # add another number and do take and advances on number ahead
            # Repeat
            for start in range(i,n+1):
                
                # Starting number
                combination.append(start)
                # All combinations with the starting number and numbers ahead excluding combinations with numbers appeared before start
                dfs(start+1)
                # For new start remove previous start
                combination.pop()

        

        dfs(1)
        return res
        