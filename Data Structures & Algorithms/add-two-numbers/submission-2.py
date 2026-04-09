# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        ### Bruteforce ###
        '''
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
        '''

        ### Traverse and Build without reversing ###
        # prev1 and prev2 are None
        # cur1 and cur2 are at heads
        # temp variable for overflows, split overflow using divide and mod by 10 
        # while one of the cur exists
        # two variables to get values, if that cur not exist that value is 0

        
        cur1, cur2 = l1, l2
        head = ListNode()
        cur = head
        prev = None
        overflow = 0
        while cur1 or cur2:

            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            total = val1 + val2 + overflow

            value = total % 10
            cur.next = ListNode(value)
            overflow = total // 10
            
            cur = cur.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        
        if overflow != 0:
            cur.next = ListNode(overflow)

        return head.next


    
            
            
            
            
            

    

        