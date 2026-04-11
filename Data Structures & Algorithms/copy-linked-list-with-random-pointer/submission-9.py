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
            print(cval, crandomval, cnextval)
            c = c.next
        """
        return dummy.next
        '''

        ### Hashmap + Linked List traverse - One Pass  ###
        
        # Hashmap maintains old to new mapping 
        hashmap = {None:None}

        # Curold points to old nodes, curnew is at dummy node.
        dummy = Node(-1)
        curold, curnew = head, dummy

        while curold:

            if curold not in hashmap:
                hashmap[curold] = Node(curold.val)
            curnew.next = hashmap[curold]

            if curold.random not in hashmap:
                hashmap[curold.random] = Node(curold.random.val)
            curnew.next.random = hashmap[curold.random]
            
            if curold.next not in hashmap:
                hashmap[curold.next] = Node(curold.next.val)
            curnew.next.next = hashmap[curold.next]
                
            curnew = curnew.next
            curold = curold.next

        c = dummy.next
        """
        while c:
            cval = c.val if c is not None else None
            cnextval = c.next.val if c.next is not None else None
            crandomval = c.random.val if c.random is not None else None
            print(cval, crandomval, cnextval)
            c = c.next
        """
        return dummy.next




