# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        ### Hashset ###
        # Traverse the linked list and put each node in hashset
        # If a node already exists that means its a cycle
        # Time : O(n)
        # Space : O(n)
        '''
        hashset = set()
        cur = head
        while cur:
            
            if cur in hashset:
                return True
            
            hashset.add(cur)
            cur = cur.next

        return False
        '''


        ### Fast and Slow pointers - Optimal ###
        # Use fast and slow pointer
        # Fast pointer can end and none or last node, as it moves two steps at a time
        # Slow pointer moves one step at a time
        # If fast and slow pointers meet anywhere than means there is a cycle
        # Time : O(n)
        # Space : O(1)

        curfast, curslow = head, head 

        while curfast and curfast.next:

            curfast = curfast.next.next
            curslow = curslow.next
            if curfast == curslow:
                return True

        return False
        
        