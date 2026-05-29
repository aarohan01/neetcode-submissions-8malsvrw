'''
## Bruteforce - add and sort each time return k
# Add -
# Time: O(m*NlogN) -> m times add called i.e for m elements * (m+n)log(m+n)  : m+n = N 
# Space: aux O(m)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.arr = nums
        self.k = k

    def add(self, val: int) -> int:

        self.arr.append(val)
        self.arr.sort()
        return self.arr[-self.k]
'''
'''
### BST add and inorder DFS with early stop ###
# Add -
# Time: O(m*h) -> m times add/m elements insert h can be logN or N
# Space: aux O(N)
class TreeNode:

    def __init__(self,val,left=None,right=None):
        self.left = left
        self.right = right
        self.val = val

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k 
        for n in nums:
            self.root = self.insert(self.root,n)

        #self.res = []
        #self.inorder(self.root,self.res)
        #print(self.res)

    def insert(self,node,val):

        if not node:
            return TreeNode(val)

        if val <= node.val:
            node.left = self.insert(node.left,val)
        else:
            node.right = self.insert(node.right,val)

        return node

    def inorder(self,node):

        if not node:
            return 

        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)


    def kthLargestVal(self, node):

        if not node:
            return 

        self.kthLargestVal(node.right)
        if self.count == 0:
            return
        self.count -= 1
        if self.count == 0:
            self.res = node.val
            return 
        
        if self.count > 0:
            self.kthLargestVal(node.left)
            


    def add(self, val: int) -> int:

        self.root = self.insert(self.root,val)
        self.count = self.k
        self.res = None
        self.kthLargestVal(self.root)
        return self.res
'''
import heapq
class KthLargest:


    ### Min heap ###
    # Min heap of k largest elements, only maintain k largest elements in the heap and return top
    # Add -
    # Time: O(m*logk)  -> m times push and/or pop, 1 push/pop log(h) i.e. logk
    # Space: aux O(k)

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
        #print(f'Add : {val} Heap : {self.minHeap}') 
        # If because the og array can have less than k already 
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]



