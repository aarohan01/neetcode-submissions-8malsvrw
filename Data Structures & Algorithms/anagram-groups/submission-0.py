class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ### Bruteforce solution ###
        # Sort each element m*nlogn (m elements) and then loop through each -
        # comparing them to other terms m*n 
        # Total m*nlogn + m*n  =  O(m*nlogn)
        '''
        res = defaultdict(list)
        for s in strs:
            #Sorts the string as a list and the rejoins as string
            sortedS = ''.join(sorted(s))
            #For each sorted key we will have a list of the unsorted forms appended
            res[sortedS].append(s)
        return list(res.values())
        '''

        ### Solution 1 ###
        # Intuition : Anagram, we can use hashset but anagrams can have repeated chars -
        # So we can use the same approach as anagram problem 
        # create dictionaries/hashmaps of all the strings recording number of each characters O(n)
        # Then loop through same length dictionaries to find anagrams and store in list
        '''
        #List of hashmaps
        hashMaps = []
        for i,n in enumerate(strs):
            hashMap = {}
            for x in n :
                hashMap[x] = hashMap.get(x,0) + 1
            hashMaps.append(hashMap)
    
        print(hashMaps)
        '''
        
        #Looping through the list of hashmaps\
        #Note that we are storing from actual array not the hashmap based on index of the hashmap in hashMaps
        '''
        result = []
        for i,n in enumerate(hashMaps):
            res = [strs[i]]
            for j,m in enumerate(hashMaps):
                if len(n) == len(m):
                    if n == m:
                        res.append(strs[j])
            result.append(res)
        
        # Loop from the next element of i 
        for i in range(len(hashMaps)):
            res = [strs[i]]
            j = i + 1 
            for j in range(len(hashMaps)-1):
                if len(hashMaps[i]) == len(hashMaps[j]):
                    if hashMaps[i] == hashMaps[j]:
                        res.append(strs[j])
            result.append(res)
        print(result)
        return result
        '''

        ### SOLUTION 3 ### 
        # After watching the video - 
        # The idea is to use the count of letters as key and use list of all the -
        # words as values.
        result = defaultdict(list)
        for word in strs:
            #List of letters
            count = [0]*26 
            #Add to the count array at position of each letter 
            for letter in word:
                count[ord(letter)-ord('a')] += 1
            
            #Since a list cannot be key (mutable) we just convert it to tuple
            #Can also use str but its a hack, it does not concatenate instead will give str representation of list
            #Best option is to use tuple of actual string conversion using map
            result[tuple(count)].append(word)

            #Other options
            #result[''.join([str(x) for x in count])].append(word)
            #result[''.join(map(str,count))].append(word)
            #result[str(count)].append(word)

        return list(result.values())

