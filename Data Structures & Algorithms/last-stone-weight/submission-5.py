import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        '''
        ### Bruteforce ###
        while len(stones) > 1:
            stones.sort()
            first = stones.pop()
            second = stones.pop()

            if first == second:
                continue
            stones.append(first-second)
        
        if stones:
            return stones[0]
        return 0  
        '''

        ### Max Heap ###
        self.stones = [ -x for x in stones ]
        heapq.heapify(self.stones)
        
        while len(self.stones) > 1:
            first = -heapq.heappop(self.stones)
            second = -heapq.heappop(self.stones)
            if first == second:
                continue
            heapq.heappush(self.stones, -(first - second))

        if self.stones:
            return -self.stones[0]
        return 0

    
