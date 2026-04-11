# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val= val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ### Bruteforce ###
        '''
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        target = len(arr) - n
        
        if target == 0:
            head = head.next
        else:
            arr[target-1].next = arr[target].next

        return head 
        '''


        ### Inplace ###

        cur = head

        # Either start from 0 and increment first or start from one and increment after moving
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        # calculated 
        target = length - n 
        print(length,target)

        prev, cur = None, head
        while target:
            prev = cur
            cur = cur.next
            target -= 1
            
        
        if prev is None:
            head = head.next 
        else:
            prev.next = cur.next
        
        return head






        ### Bruteforce ###
        # Put nodes in array, calculate previous node index.
        # If previous node is negative that means first node is removed just reattach head
        # Else attach previous node to next nodes next.
        '''
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        
        # Previous node index from start of array based on n, n is from 1 and start is from 0 
        prev = (len(arr) - 1) - n 

        # If first node is to be removed else any other
        if prev == -1:
            head = arr[prev + 1].next 
        else: 
            arr[prev].next = arr[prev].next.next

        return head
        '''

        ### Inplace ###
        '''
        midnode = 1
        fast, slow = head, head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            midnode += 1
        
        # Total nodes 
        tnodes = midnode * 2 - 1 if fast else midnode * 2 - 2
        print(tnodes)

        # Steps to travel to reach node before n 
        steps = tnodes - n - 1
        print(steps)

        # First Node or any other node 
        if steps == -1:
            head = head.next
        else:
            cur = head 
            while steps:
                cur = cur.next
                steps -= 1
            cur.next = cur.next.next
        
        return head
        '''
        





        