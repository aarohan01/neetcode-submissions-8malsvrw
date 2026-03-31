from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ### Bruteforce ###
        # Atleast 1 point given, order isn't important other wise would have had to preserve order
        # Can't use dictionary coz values can be same
        # Calculate distances + sort + give first two 
        # Time :O(n) + O(nlogn) + O(2) = O(nlogn)
        # Space : O(n) + O(1) + O(k) = O(n)

        '''
        distances = [ (sqrt(i[0]**2 + i[1]**2),i) for i in points ]
        distances.sort()
        result = [ distances[i][1] for i in range(k) ]
        return result
        '''        

        ### MinHeap 1 ### 
        # Using minHeap to store the values 
        # calculate all distances + heapify + pop 
        # Time : O(n) + O(n) + O(klogn) = O(nlogn) becoz k can be equal to n
        # Space : O(n) + O(n) + O(k) = O(n)
        '''
        minHeap =  [(sqrt(i[0]**2 + i[1]**2),i) for i in points ]
        heapq.heapify(minHeap)
        result = [heapq.heappop(minHeap)[1] for i in range(k)]
        return result
        '''


        ### MaxHeap : Only store k values in heap ###
        # Calculate distance and push to max heap. If lenght of heap greater than k then pop
        # Once processed all points return the heap as array
        # calculate distances + pop + pop output
        # Time : O(n) + O(nlogk)  -> since we ultimately pop all elments 
        # Space : O(k)

        maxHeap = []
        heapq.heapify(maxHeap) 

        for i in points:

            #squared distance
            distance = i[0]**2 + i[1]**2
            heapq.heappush(maxHeap,(-distance,i)) 
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [ i[1] for i in maxHeap ]
        
        
