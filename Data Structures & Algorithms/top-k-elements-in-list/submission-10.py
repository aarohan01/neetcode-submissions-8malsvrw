import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        ### Bruteforce / Naive solution ###
        # Idea : store frequency of each number sort it and output 
        # Time : O(nlogn) -> worst case every number is unique sorting will dominate
        # Space : O(n)
        '''
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        print(hashmap)
        
        # Sort the dict based on values in desc
        # Little difficult
        #res = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        #result = [ x for x,y in res[:k]]
        

        # Loop though the dict and convert to tuples and sort
        res = []
        for key, val in hashmap.items():
	        res.append((val, key))
        res.sort(reverse=True)


        result = [ y for x,y in res[:k]]
    
        return result 
        '''


        ### MinHeap ###
        # Store the tuples in list and heapify instead of sorting 
        # Time : O(nlogk) : Freq + Heappush + Pop : n + nlogk + klogk
        # Space : O(n+k)
        '''
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        print(hashmap)

        # MinHeap of k elements
        res = []
        heapq.heapify(res)
        for key, val in hashmap.items():
            heapq.heappush(res,(val, key))
            if len(res) > k:
                heapq.heappop(res)
        print(res)
        
        # Pop one by one 
        result = []
        while res:
            result.append(heapq.heappop(res)[1])
        return result
        '''

        ### Bucket Sort ###
        ## Max freq cannot be more that length of nums

        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        print(hashmap)


        res = [[] for i in range(len(nums)+1)]
        print(res)

        for key, val in hashmap.items():
            print(f'{val}-{key}')
            res[val].append(key)
        
        print(res)

        # Loop throught the buckets in reverse 
        result = []
        for i in range(len(res)-1, 0 ,-1):
            for j in res[i]:
                result.append(j)
                if len(result) == k:
                    return result
            







