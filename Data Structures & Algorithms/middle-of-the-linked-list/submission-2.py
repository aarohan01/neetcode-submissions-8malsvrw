# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


        ### Bruteforce ###
        # Put everything in an array and give middle
        # Time: O(n)
        # Time : O(n)
        '''
        arr = []
        cur = head 

        while cur:
            arr.append(cur)
            cur = cur.next
        
        return arr[len(arr)//2]
        '''

        ### Fast and slow pointers ###
        
        curfast, curslow =  head, head
        
        while curfast and curfast.next:

            curfast = curfast.next.next
            curslow = curslow.next

        return curslow

