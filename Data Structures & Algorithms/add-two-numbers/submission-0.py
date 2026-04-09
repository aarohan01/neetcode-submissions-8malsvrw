# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        ### Bruteforce ###
        num1, num2 = [], []

        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next

        n1 = int(''.join(num1[::-1])) if num1 else 0
        n2 = int(''.join(num2[::-1])) if num2 else 0
        print(n1,n2)

        t = str(n1 + n2)
        print(t)
    
        
        
        head = ListNode()
        cur = head
        for i in range(len(t)-1,-1,-1):
            
            cur.next = ListNode(int(t[i]))
            cur = cur.next
        
        return head.next
    
            
            
            
            
            

    

        