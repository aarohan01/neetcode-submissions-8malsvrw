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
        '''
        # MaxHeap
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        print(maxHeap)

        for i in range(k):
            res = -heapq.heappop(maxHeap)
        
        return res
        '''

        ### Solution 2 : MinHeap - Optimal ###
        # Only store the k elements in the heap by popping if len greater than k
        # Then pop the remaining elements
        # Total elements pushed or popped will be n
        # Time : O(nlogk)
        # Space : O(k)

        minHeap = []
        heapq.heapify(minHeap)

        for i in nums:
            heapq.heappush(minHeap,i)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return heapq.heappop(minHeap)


        ### Solution 3 : QuickSelect - Optimal ###
        ## MinHeap is optimal if k is small, and/or streaming input or very large array or doing multiple times
        ## QuickSelect - For onehot if array can fit in the memory or array not sorted etc
