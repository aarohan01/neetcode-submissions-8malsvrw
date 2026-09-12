class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        hashmap = {}
        for i in strs:
            
            sortedi =  str(sorted(i))
            if sortedi not in hashmap:
                hashmap[sortedi] = []
            hashmap[sortedi].append(i)
        
        return list(hashmap.values())
        '''

        def freqmap(string):

            arr = [0]*26
            for i in string:
                arr[ord(i)-ord('a')] += 1

            return tuple(arr)
        
        hashmap = {}
        for s in strs:

            freqs = freqmap(s)
            if freqs not in hashmap:
                hashmap[freqs] = []
            
            hashmap[freqs].append(s)

        return list(hashmap.values())
