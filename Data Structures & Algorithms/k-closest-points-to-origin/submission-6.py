class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:



        ### Bruteforce ###
        dist = []
        for x,y in points:
            d = (0-x)**2 + (0-y)**2
            dist.append([d,[x,y]])

        dist.sort()
        return [x[1] for x in dist[:k]]
        

        