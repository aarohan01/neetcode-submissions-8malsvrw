import heapq

class KthLargest:

    ### Solutions Intuition ###
    ## Bruteforce - Sort the array +  add and sort each time + update k
    # O(nlogn) + m*NlogN + O(1) = O(m*NlogN) where m is added elements, N=(m+n)
    ## Solution 1 - Sort + Binary Search + add + update k
    # O(nlogn) + O(m*logN) +(m*N) + O(1) = O(mN) 
    # since adding to an array in worst case i.e middle can be O(N)
    ## Solution 2 - Binary Search Tree create + insert + update k
    # O(n) + O(m*N) + O(N) = O(mN) 
    # In worst case scenarion unbalanced binary tree creation is O(N) same for insert.
    ## Final Solution ##
    # Min heap of k largest elements, only maintain k largest elements in the heap and return top

    def __init__(self, k: int, nums: List[int]):

        # Given : Atlest k elements in the heap and we don't remove any elements,BUT 
        # when testing there appears to be empty arrays and till k size
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        # Remove elements till only k elements:
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:

        
        heapq.heappush(self.minHeap,val)
        print(f'Add : {val} Heap : {self.minHeap}') 
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]



