class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ### Bruteforce 
        '''
        hashmap = {}
        for word in strs:
            sword = ''.join(sorted(word))
            if sword in hashmap:
                hashmap[sword].append(word)
            else:
                hashmap[sword] = [word]

        result = [ val for key, val in hashmap.items()]
        return result
        '''

        ### freq table 

        def getTable(word):

            res = [0]*26
            for letter in word:
                index = ord(letter) - ord('a')
                res[index] += 1

            return tuple(res) 


        hashmap = {}
        for word in strs:
            tword = getTable(word) 
            if tword not in hashmap:
                hashmap[tword] = [word]
            else:
                hashmap[tword].append(word)
        
        result = [ val for key, val in hashmap.items()]
        return result
        
            