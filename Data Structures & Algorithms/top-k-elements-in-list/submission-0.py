class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        ### Bruteforce / Naive solution ###
        # Idea : store frequency of each number sort it and output 
        # Time : O(nlogn) -> worst case every number is unique sorting will dominate
        # Space : O(n)
        
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        print(hashmap)

        res = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        
        result = [ x for x,y in res[:k]]
        return result