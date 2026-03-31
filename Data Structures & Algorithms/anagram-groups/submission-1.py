class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        ### Bruteforce ###
        # Use an array instead of hashmap as a key.
        # For every sorted string get the index and attach
        # Not worth thinking for this problem


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
            


        
                    

        