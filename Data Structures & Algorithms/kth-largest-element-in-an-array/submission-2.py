import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ### Bruteforce ###
        # Sort and return the k th element
        # Sort inplace + return 
        # Time : O(nlogn) + O(1) = O(nlogn)
        # Space : O(1)
        '''
        if nums and len(nums)>0:
            nums.sort()
            return nums[-k]
        return 
        '''

        ### Solution 1 : MaxHeap ###
        # Heapify and pop the k values 
        # Heapify + pop k 
        # Time : O(n) + (klogn)
        # Space : O(n)

        # MaxHeap
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        print(maxHeap)

        for i in range(k):
            res = -heapq.heappop(maxHeap)
        
        return res
