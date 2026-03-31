class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        
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