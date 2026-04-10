# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        ### Bruteforce ###
        # Convert to list and use two pointers plus construct a linked list using another pointer

        cur1, cur2 = list1, list2
        arr1, arr2 = [], []

        while cur1:
            arr1.append(cur1.val)
            cur1 = cur1.next

        while cur2:
            arr2.append(cur2.val)
            cur2 = cur2.next
        
        print(arr1,arr2)

        l1, l2 = 0, 0
        head = ListNode()
        cur = head
        while l1 < len(arr1) or l2 < len(arr2):

            if l1 >= len(arr1):
                val = arr2[l2]
                l2 += 1 
            elif l2 >= len(arr2):
                val = arr1[l1]
                l1 += 1
            else:
                if arr1[l1] <= arr2[l2]:
                    val = arr1[l1]
                    l1 += 1
                else:
                    val = arr2[l2]
                    l2 += 1

            
            cur.next = ListNode(val)
            cur = cur.next

        
        return head.next
            
        