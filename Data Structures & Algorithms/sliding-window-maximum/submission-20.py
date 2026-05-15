import heapq
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ### Bruteforce ###
        '''
        res = []
        for L in range(len(nums)-k+1):
            curmax = nums[L]
            for R in range(L+1,L+k):
                curmax = max(curmax,nums[R])
                print(curmax)
            res.append(curmax)
        return res
        '''

        ### Sliding window and Maxheap ###
        '''
        L = 0
        maxheap = []
        res = []
        for R in range(len(nums)):
            #print(R)
            heapq.heappush(maxheap,(-nums[R],R))

            if R - L + 1 >= k:
                #print(maxheap)  
                res.append(-maxheap[0][0])
                #print(res)
                while maxheap and maxheap[0][1] <= L:
                    heapq.heappop(maxheap)
                L += 1
            
        return res
        '''

        ### Deque + Sliding window ###
        # Need to get max cheaply but also need to maintain order therefore a monotonic queue can be used instead 
        # of heap as heap cannot maintain order
        # For each element add its index the queue but first check if any existing elements are larger if yes pop them
        # Expand window using R while adding, if window reaches k add the top element to res and then check if its index is out of 
        # window if yes popleft using L
        # Time: O(n)
        # Space : O(n)
        '''
        queue = deque()
        L = 0
        res = []

        for R in range(len(nums)):
            # If not empty then first check if value inside queue is lesser if yes then pop to maintain order
            while queue and queue[-1][0] < nums[R]:
                queue.pop()
            # Append in anycase
            queue.append((nums[R], R))
            #print(queue)

            # If equal or more than window elements in queue
            if R - L + 1 >= k:
                res.append(queue[0][0])
                #print(res)
                # Window overflow
                if queue[0][1] <= L:
                    queue.popleft()
                L += 1

        return res
        '''

        ### Same but using just index version ###
        # Do any which seems easier 

        queue = deque()
        L = 0
        res = []
        
        for R in range(len(nums)):
            
            ### Maintain monotonic nature of queue to keep max at end
            while queue and nums[queue[-1]] < nums[R]:
                queue.pop()

            queue.append(R)


            ### Fill the queue and empty the queue based on window
            if R - L + 1 >= k:
                res.append(nums[queue[0]])
        
                if queue[0] == L:
                    queue.popleft()
        
                L += 1
        
        return res

            











        