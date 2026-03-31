import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        ### 
        '''
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1

        res = []
        for i in hashMap:
            res.append((hashMap[i],i))

        res.sort(reverse=True)

        result = []
        for i in range(k):

            result.append(res[i][1])
        return result
        '''

        ### MinHeap ###
        '''
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1

        heap = []
        for num, freq in hashMap.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res
        '''
        ### Bucket sort 
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1

        res = [[] for _ in range(len(nums)+ 1) ]

        for num, freq in hashMap.items():

            res[freq].append(num)
        
        result = []
        for freq in range(len(res)-1,0,-1):
            for num in res[freq]:
                result.append(num)
                if len(result) >= k:
                    return result

                
    
        
            

            


