class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hashmap = {}

        for i in strs:
            
            sortedi =  str(sorted(i))
            if sortedi not in hashmap:
                hashmap[sortedi] = []
            hashmap[sortedi].append(i)
        
        return list(hashmap.values())
