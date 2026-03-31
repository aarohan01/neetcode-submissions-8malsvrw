class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        

    def push(self, val: int) -> None:
        
        # Append to the end
        self.heap.append(val)
        
        # Percolate to top if min. i index of the last element
        i = len(self.heap) - 1 

        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def percolateDown(self,i: int) -> None:

        while 2*i < len(self.heap):

            # Case 1 : Right child also exists and its lower than left child and i greater than that
            if 2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[i] > self.heap[2*i+1]:

                # Swap 
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i+1

            # Case 2 : Left child exists and its lower than i
            elif self.heap[i] > self.heap[2*i]:

                # Swap 
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i

            # Case 3 : Its already in min position
            else:
                break


    def pop(self) -> int:

        # If empty return None if only 1 element just pop 
        if len(self.heap) == 1:
            return -1
        
        # Only 1 element in heap
        if len(self.heap) == 2:
            return self.heap.pop()
        
        # Multiple elements
        res = self.heap[1]
        
        # Get last element on top and percolate to bottom
        i = 1 
        self.heap[1] = self.heap.pop()

        # minimum of left and right child will go to parent to maintain structure property
        # Until there are any left children
        self.percolateDown(i)

        return res

        

    def top(self) -> int:
        
        # Empty
        if len(self.heap) <= 1:
            return -1
        return self.heap[1]


    def heapify(self, nums: List[int]) -> None:

        # Empty List
        if not nums:
            return 

        # First element append to end, then first node is now dummy with its value secured
        self.heap = nums + [nums[0]]

        # Skip leaf node percolation to top
        mid = len(self.heap)-1//2

        # Percolate each element to down, i goes to 1, mid+1 will be skipped 
        for i in reversed(range(1,mid+1)):

            self.percolateDown(i)




        
        