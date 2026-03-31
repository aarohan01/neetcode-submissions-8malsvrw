from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ### Bruteforce ###
        # Atleast 1 point given, order isn't important other wise would have had to preserve order
        # Can't use dictionary coz values can be same
        # Calculate distances + sort + give first two 
        # O(n) + O(nlogn) + O(2) = O(nlogn)

        '''
        distances = [ (sqrt(i[0]**2 + i[1]**2),i) for i in points ]
        distances.sort()
        result = [ distances[i][1] for i in range(k) ]
        return result
        '''        
        minHeap =  [(sqrt(i[0]**2 + i[1]**2),i) for i in points ]
        heapq.heapify(minHeap)
        result = [heapq.heappop(minHeap)[1] for i in range(k)]
        return result
        


