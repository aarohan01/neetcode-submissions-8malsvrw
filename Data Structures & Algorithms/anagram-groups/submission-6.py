class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ### Bruteforce 

        hashmap = {}
        for word in strs:
            sword = ''.join(sorted(word))
            if sword in hashmap:
                hashmap[sword].append(word)
            else:
                hashmap[sword] = [word]

        result = [ val for key, val in hashmap.items()]
        return result
        