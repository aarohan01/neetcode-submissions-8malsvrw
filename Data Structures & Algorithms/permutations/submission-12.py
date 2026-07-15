class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        ### Backtracking permutaion no dupes ###
        # Order matters, no dupes hence permutaition normal
        # TAKE + record take + START OVER 
        # The idea is similar to combination but instead of for-loop ahead, we for loop all except already visited in path
        # Since we for loop all every time we don't need to pass as its fresh in each call
        # But to maintain in the current path what we have already visited we have a global array 
        # In permutaion we are trying from each i the remaining i's then remaining...till length is equal to nums
        # Then do it again with a different start i
        # Base case 1 : if perm length equal to nums : Success
        # Choice 1 : Take the nums[i], record it in visited, then Start over
        # Once the base case is reached we backtrack by doing undo and removing the choices 
        # 1 -> 2 -> 3 -> 4 then backtrack to 1 -> 2 then go to 1 -> 2 -> 4 -> 3 then backtrack to 1 -> 3...and so on
        # Time: O(n * n!) -> n! permutations and n copy every time nPn is n!
        # Space: O(n) aux-> O(n) for perm + O(n) for visited + O(n) for recursion stack
        # Output space is n * n! since n! permutations containing n elements
        '''
        # res : all permutaions perms : current permutation
        res, perms = [], []

        # visited array to maintain which indexed already visited for a path (global shared accross a path)
        visited = [False]*len(nums)

        # For each index i of nums we create a path based on visited
        def dfs():
            #print(perms)
            if len(perms) == len(nums):
                res.append(perms.copy())
                return 

            # For every i take i then based on visited take other i untill len()
            for i in range(len(nums)):

                # Take and start over
                if not visited[i]:
                    perms.append(nums[i])
                    visited[i] = True
                    dfs()
                    
                    # Undo / Backtrack
                    perms.pop()
                    visited[i] = False
        dfs()
        return res
        '''


        ### Little more optimized using bitmask instead of visited array ###
        # Note that checking the lsb for set or not 
        # Then setting it using OR 
        # To unset is AND with negative
        # Can also use XOR flip but this is better more accurate in the sense of understanding
        # Time: O(n * n!)
        # Space: O(n) aux -> O(n) perm + O(n) recursion stack we avoided O(n) for visited array
        # Output space is n * n! since n! permutations containing n elements

        # res : all permutaions perms : current permutation
        res, perms = [], []

        # visited bitmask to maintain which indexed already visited for a path (global shared accross a path)
        visited = 0

        # For each index i of nums we create a path based on visited
        def dfs():
            nonlocal visited 
            #print(perms)
            if len(perms) == len(nums):
                res.append(perms.copy())
                return 

            # For every i take i then based on visited take other i untill len()
            for i in range(len(nums)):
                

                # Take and start over
                if visited & (1 << i) == 0:
                    perms.append(nums[i])
                    visited |= (1 << i)
                    dfs()
                    
                    # Undo / Backtrack
                    perms.pop()
                    visited &= ~(1 << i)
                    
        dfs()
        return res
