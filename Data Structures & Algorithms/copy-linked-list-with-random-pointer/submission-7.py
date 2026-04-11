"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        
        ### Hashmap + Linked List traverse - Two Pass  ###
        # Time: O(n)
        # Space: O(n)

        '''
        # Hashmap maintains old to new mapping 
        hashmap = {}

        # Curold points to old nodes, curnew is at dummy node.
        dummy = Node(-1)
        curold, curnew = head, dummy

        while curold:
            curnew.next = Node(curold.val)
            hashmap[curold] = curnew.next
            curnew = curnew.next
            curold = curold.next

        #print([(x.val,y.val) for x,y in hashmap.items()])

        curold = head
        while curold:
            
            # Somtimes the curold.next or curold.random will be None and thus not in the hashmap
            # Another option is to put {None:None} in the hashmap itself
            nextval = hashmap[curold.next] if curold.next in hashmap else None
            randomval = hashmap[curold.random] if curold.random in hashmap else None

            # The mapped new node to mapped new node based on hashmap pair
            hashmap[curold].next = nextval
            hashmap[curold].random = randomval

            curold = curold.next
        
        ### Test ###
        """
        c = dummy.next
        while c:
            cval = c.val if c is not None else None
            cnextval = c.next.val if c.next is not None else None
            crandomval = c.random.val if c.random is not None else None
            print(cval,cnextval,crandomval)
            c = c.next
        """
        return dummy.next
        '''

        ### Hashmap + Linked List traverse - One Pass  ###
        
        # Hashmap maintains old to new mapping 
        hashmap = {None: None}

        def getClone(node):
            if node not in hashmap:
                hashmap[node] = Node(node.val)
            return hashmap[node]

        # Curold points to old nodes, curnew is at dummy node.
        dummy = Node(-1)
        curold, curnew = head, dummy

        while curold:
            curnew.next = getClone(curold)
            curnew.next.next = getClone(curold.next)
            curnew.next.random = getClone(curold.random)
            
            curnew = curnew.next
            curold = curold.next
        
        return dummy.next