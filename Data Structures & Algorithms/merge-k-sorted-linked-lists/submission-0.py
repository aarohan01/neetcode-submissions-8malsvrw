# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ### Bruteforce ###
        # Traverse all the linked list and put it in an array
        # Sort the array and recreate a linked list

        res = []

        def traverse( link: list ) -> None:

            if not link:
                return

            cur = link
            while cur:
                res.append(cur.val)
                cur = cur.next
        
        if not list:
            return 

        for l in lists:
            traverse(l)
        
        print(res)

        res.sort()

        dummy = ListNode()
        cur = dummy 

        for i in res:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        
        return dummy.next
        

            