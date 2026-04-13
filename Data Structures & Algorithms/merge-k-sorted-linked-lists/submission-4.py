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
        # Time: O(NlogN)  --> Where N is the total number of nodes
        # Space: O(N)
        '''
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


        res.sort()

        dummy = ListNode()
        cur = dummy 

        for i in res:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        
        return dummy.next
        '''

        ### Merge One by One ###

        if not lists or len(lists) <= 1:
            return 
        
        def mergeLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

            cur1, cur2 = list1, list2
            
            dummy = ListNode()
            cur = dummy

            while cur1 and cur2:
                
                if cur1.val <= cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                
                cur = cur.next
            
            if cur1:
                cur.next = cur1
            else:
                cur.next = cur2
            
            return dummy.next


        head = mergeLists(lists[0], lists[1])
        for i in range(2,len(lists)):
            head = mergeLists(head, lists[i])

        return head


        
        

            