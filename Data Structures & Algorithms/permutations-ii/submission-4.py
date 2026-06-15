class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ### Backtracking permutaion with dupes ###
        # Order matters,  dupes in input hence permutaition dupes
        # SORT + TAKE ONLY ONE occurence at a level + record take + START OVER 
        # The idea is similar to combination but instead of for-loop ahead, we for loop all except already used in path
        # Since we for loop all every time we don't need to pass as its fresh in each call
        # But to maintain in the current path what we have already used we have a global array 
        # In permutaion we are trying from each i the remaining i's then remaining...till length is equal to nums
        # Then do it again with a different start i
        # Base case 1 : if perm length equal to nums : Success
        # Choice 1 : Take the nums[i], record it in used, then Start over
        # Once the base case is reached we backtrack by doing undo and removing the choices 
        # 1 -> 2 -> 3 -> 4 then backtrack to 1 -> 2 then go to 1 -> 2 -> 4 -> 3 then backtrack to 1 -> 3...and so on
        # Time: O(n * n!) -> n! permutations and n copy every time nPn is n!  
        #### If n terms were unique that would be the worst case scenario thus n! * n
        # Space: O(n) aux-> O(n) for perm + O(n) for used + O(n) for recursion stack
        # Output space is n * n! since n! permutations containing n elements
        
        '''
        #### Sort ####
        nums.sort()

        # res : all permutaions perms : current permutation
        res, perms = [], []

        # Used array to maintain which indexed already used for a path (global shared accross a path)
        used = [False]*len(nums)

        # For each index i of nums we create a path based on used
        def dfs():
            #print(perms)
            if len(perms) == len(nums):
                res.append(perms.copy())
                return 

            # For every i take i then based on used take other i untill len()
            for i in range(len(nums)):

                # Take and start over
                if not used[i]:
                    
                    ### Skip i if i+1 is same and i+1 is not yet set to true ###
                    ## Because once i+1 is set to true in the next recursion i will be used since i+1 will be true
                    ## Easier explanation -> if the number is same and its ahead number is visited then fine else continue
                    if (i + 1) < len(nums) and nums[i] == nums[i + 1] and not used[i + 1]:
                        continue

                    #OR

                    ### Skip i if i-1 was same and i-1 set to true ###
                    #if (i - 1) >= 0 and nums[i] == nums[i - 1] and not used[i-1]:
                        #continue

                    perms.append(nums[i])
                    used[i] = True
                    dfs()
                    
                    # Undo / Backtrack
                    perms.pop()
                    used[i] = False

                    

        dfs()
        return res
        '''


        ### Little more optimized using bitmask instead of used array ###
        # Note that checking the lsb for set or not 
        # Then setting it using OR 
        # To unset is AND with negative
        # Can also use XOR flip but this is better more accurate in the sense of understanding
        # Time: O(n * n!)
        # Space: O(n) aux -> O(n) perm + O(n) recursion stack we avoided O(n) for used array
        # Output space is n * n! since n! permutations containing n elements
        

        #### SORT ####
        nums.sort()

        # res : all permutaions perms : current permutation
        res, perms = [], []

        # Used bitmask to maintain which indexed already used for a path (global shared accross a path)
        used = 0

        # For each index i of nums we create a path based on used
        def dfs():
            nonlocal used 
            #print(perms)
            if len(perms) == len(nums):
                res.append(perms.copy())
                return 

            # For every i take i then based on used take other i untill len()
            for i in range(len(nums)):
                

                # Take and start over
                if (used >> i) & 1 == 0:
                    

                    if (i+1) < len(nums) and nums[i] == nums[i+1]  and (used >> (i+1)) & 1 ==  0:
                        continue


                    perms.append(nums[i])
                    used |= (1 << i)
                    dfs()
                    
                    # Undo / Backtrack
                    perms.pop()
                    used &= ~(1 << i)
                    
        dfs()
        return res
        