class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        ### Bruteforce ###
        # Sort the strings in the array. Use a set as keys to match.
        # Loop through set and sorted strings and store the results if matching the key in set.
        # Time : O(n^2)   : n*mlogm + n*m + n^2*m : Sort + Set creation + looping where m is length of max word
        # Space : O(n*m) : O(3n*m)
        '''

        # Edge cases
        if not strs or len(strs) <= 1:
            return [strs]

        
        sstrs = [''.join(sorted(i)) for i in strs ]
        sstrs_set = set(sstrs)
        
        result = []

        for i in sstrs_set:
            res = []

            for j in range(len(sstrs)):

                if i == sstrs[j]:
                    res.append(strs[j])
            
            result.append(res)
        
        return result
            
        '''


        ### HashMap ###
        # Use sorted string as key.
        # Use hashmap to store the key when a word is first discovered else append the values of that key with value.
        # 

        HashMap = {}

        for s in range(len(strs)):
            
            # Sorted string to match keys
            ss = ''.join(sorted(strs[s]))

            if ss not in HashMap:
                HashMap[ss] = [strs[s]]
            else:
                HashMap[ss].append(strs[s])
            
        result = [ HashMap[i] for i in HashMap]
        return result


        
                    

        