import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:



        ### Bruteforce ###
        dist = []
        for x,y in points:
            d = (0-x)**2 + (0-y)**2
            dist.append([d,[x,y]])

        dist.sort()
        return [dist[x][1] for x in range(k)]


        ### maxheap ###
        maxheap = []
        
        for x,y in points:
            d = (0-x)**2 + (0-y)**2
            heapq.heappush(maxheap,(-d,[x,y]))

            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        res = []
        while maxheap:
            r = heapq.heappop(maxheap)
            res.append(r[1])
        return res
        