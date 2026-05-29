import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        '''
        ### Bruteforce ###
        # Time: O(n^2logn)  -> n elements sorted nlogn then n operations times
        # Space: O(1) aux
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
        # Form max heap, pop the first two 
        # if equal do nothing 
        # if first is bigger push first-second 
        # Do this while atleast one element in heap return that 
        # Time: O(nlogn)  -> n elements inserted/pushed into heap for creation -> push is log(h) i.e. logn
        # Space: O(n)
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

        ### Bucket sort : Do later ###
