class TreeNode:

    def __init__(self, key, val):

        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        
        # In BST we generally insert in the leaf node OR USE ITERATIVE SOLUTION 
        # Base case : Reached leaf, return the new node to parent's left or right
        
        '''
        if not self.root:
            print(f'k:{key} v:{val}')
            return TreeNode( key, val )
        
        # Based on key look for position 
        if key < self.root.key:
            self.root.left = self.insert( key, val)
        elif key > self.root.key:
            self.root.right = self.insert( key, val)
        else:
            self.root.val = val
            # OR 
            # self.root = TreeNode( Key, val )
        
        # Return the root to parent if not leaf 
        return self.root
        '''

        def insertHelper( node, key, val ):

            
            if not node:
                print(f'k:{key} v:{val}')
                return TreeNode( key, val )
            print(f'Inserting node:{node.key} key:{key} val:{val}')
            # Based on key look for position 
            if key < node.key:
                node.left = insertHelper(  node.left, key, val )
            elif key > node.key:
                node.right = insertHelper( node.right, key, val )
            else:
                node.val = val
                # OR the unhashed is better way
                #node = TreeNode( key, val )
            
            # Return the root to parent if not leaf 
            return node

        self.root = insertHelper( self.root, key, val)



    def get(self, key: int) -> int:

        # Need to search the key and return the value 
        # Can be done using recursion or iterative

        # Search closure function OR USE ITERATIVE SOLUTION 
        def search( node, key ):


            if not node:
                return 
        
            if key < node.key:
                return search( node.left, key )
            elif key > node.key:
                return search ( node.right, key )
            else:
                return node 
        
        result = search(self.root, key)
        if result:
            #print(f'Get k:{key} v:{result.val}')
            return result.val
        return -1
            

    def getMin(self) -> int:

        # Return value of the leftmost node's key
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        
        if curr:
            return curr.val
        return -1


    def getMax(self) -> int:
        
        # Return value of rightmost node's key
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        
        if curr:
            return curr.val
        return -1


    def remove(self, key: int) -> None:

        # Removal has two cases  
        # Case 1 : 0 or 1 child -
        #   Case 1.1 - 0 child then no issues 
        #   Case 1.2 - If one child i.e make other child the parent
        # Case 2 : 2 children 
        #   In this case make the leftmost node of the right subtree the parent
        # Then delete that node


        def removeHelper( node, key ):

            if not node:
                return 
            
            if key < node.key:
                node.left = removeHelper( node, key)
            elif key > node.key:
                node.right = removeHelper( node, key)
            else:
                
                # Case 1.1 just returns
                # Case 1.2 : 
                if not node.left:
                    return node.right 
                elif not node.right:
                    return node.left
                else:

                    curr = node.right 
                    while curr and curr.left:
                        curr = curr.left
                    minNode = curr
                    node.key, node.val = minNode.key, minNode.val 
                    node.right = removeHelper(node.right, minNode.key)
            
            return node
        
        self.root = removeHelper(self.root,key)

        


    def getInorderKeys(self) -> List[int]:

        # DFS 

        self.res = []

        # Closure function inorder DFS
        def dfs(node: Optional[TreeNode]) -> None:

            if not node:
                return 
            
            dfs(node.left)
            self.res.append(node.key)
            dfs(node.right)


        dfs(self.root)
        print(f'IgnoreKeys : {self.res}')
        return self.res


