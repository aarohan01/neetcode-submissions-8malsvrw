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

        
        


        
