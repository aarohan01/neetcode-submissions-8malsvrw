class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        ### 
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1

        res = []
        for i in hashMap:
            res.append((hashMap[i],i))

        res.sort(reverse=True)

        result = []
        for i in range(k):
            print(i)
            result.append(res[i][1])
        return result