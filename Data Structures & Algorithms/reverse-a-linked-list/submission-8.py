# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        ### Bruteforce ###
        # Traverse and put values in array 
        # Reconstruct the linked list in reverse order of array
        # Time: O(n)
        # Space : O(n)
        '''
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next

        print(arr)

        head = ListNode()
        cur = head
        for i in range(len(arr)-1,-1,-1):

            cur.next = ListNode(arr[i])
            cur = cur.next

        return head.next
        '''

        ### Inplace ###
        prev, cur = None, head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

        