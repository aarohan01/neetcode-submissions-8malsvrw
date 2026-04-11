# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val= val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        ### Bruteforce ###
        # Put nodes in array, calculate distance to n from front and 
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


        