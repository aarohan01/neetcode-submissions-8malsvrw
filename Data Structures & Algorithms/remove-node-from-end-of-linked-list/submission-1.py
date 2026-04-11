# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        ### Bruteforce ###
        
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        

        l = len(arr) - n - 1

        if l == -1:
            head = arr[l+1].next 
        else: 
            arr[l].next = arr[l].next.next

        return head


        