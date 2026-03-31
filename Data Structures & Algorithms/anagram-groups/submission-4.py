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
        # Time : O(n*mlogm) : n*mlogm + n*m + n*m :Sort in loop + add to dictionary all n items + get values from hashmap 
        # Space : O(n*m)
        '''

        # Edge cases
        if not strs or len(strs) <= 1:
            return [strs]
        
        HashMap = {}

        for s in range(len(strs)):
            
            # Sorted string to match keys
            ss = ''.join(sorted(strs[s]))

            if ss not in HashMap:
                HashMap[ss] = [strs[s]]
            else:
                HashMap[ss].append(strs[s])
            
        result = [ HashMap[i] for i in HashMap ]
        return result
        '''

        ### HashTable ###
        # For each string create a hashtable for each string and use it as key in hashmap to compare
        # This avoids sorting and instead uses frequency of characters to compare.
        # Time : O(n*m) -> avoids sorting the strings of lenght m
        # Space : O(n*m)

        # Edge cases
        if not strs or len(strs) <= 1:
            return [strs]

        def hashtable(string):

            table = [0]*26
            for c in string:
                index = ord(c) - ord('a')
                table[index] += 1
            return tuple(table)


        hashmap = {}
        for s in strs:

            if hashtable(s) not in hashmap:
                hashmap[hashtable(s)] = [s]
            else:
                hashmap[hashtable(s)].append(s)
        
        return list(hashmap.values())

       

        



        
                    

        