# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        ### Bruteforce ###
        ## Arrange in the list first and then connect the nodes ##
        # Time : O(n)
        # Space : O(n)
        '''
        if not head
        w = k
        
        while w <= len(res):
            
            L, R = w-k, w-1
            print(f'w:{w}')
            while L < R:
                print(f'r:{R} l:{L}')
                res[L], res[R] = res[R], res[L]
                L += 1
                R -= 1
            
            w += k
        

        
        for cur in range(len(res)):

            res[cur].next = res[cur+1] if cur+1 < len(res) else None
        
        print([(r.val,r.next.val) for r in res if r.next is not None])

        return res[0]
        '''
        

        ### Two Pass inplace ###
        ## Get the lenght then loop accordingly ##
        '''
        length = 0

        cur = head
        while cur:
            length += 1
            cur = cur.next

        print(length)


        prev, cur = None, head
        count = 0

        while cur:
        '''

        '''
        def reverse(curslow, curfast, prevslow):
            
            prev = curfast
            cur = curslow
            while cur != curfast:
                print(prev.val if prev else None)
                tmp = cur.next 
                cur.next = prev
                pval = prev.val if prev else None
                cval = cur.val if cur else None
                print(f'Conncected : {cval} to {pval}')

                prev = cur
                cur = tmp

        
        

        curslow, curfast = head, head
        dummy = ListNode()
        prevslow = dummy 
        res = None
        while curslow:
            
            count = 0
            while count < k:
                curfast = curfast.next 
                count += 1
                if count < k and curfast == None:
                    return dummy.next
            
            cf = curfast.val if curfast else None
            cs = curslow.val if curslow else None
            print(f'cs {cs} cf:{cf}')


            prevslow.next = reverse(curslow, curfast)

            curslow = curfast
            if curslow:
                print(f'curslow {curslow.val}')


        return dummy.next
        '''

        

        def reverse():
            
            nonlocal curslow, curfast
        
            prev, last = None, curslow
            print(head.val)
            while curslow != curfast:
                tmp = curslow.next
                curslow.next = prev
                pval = prev.val if prev else None
                print(f'Connected {curslow.val} to {pval}')
                prev = curslow
                curslow = tmp
            

            last.next = curslow
            return prev, last
        
        
        dummy = ListNode()
        dummy.next = head
        curfast, curslow = head, head
        


        while curslow:
            nodecount = 0
            while nodecount != k:
                curfast = curfast.next
                nodecount += 1
                if nodecount <= k-1 and curfast is None:
                    return dummy.next
            
        
        
            #print(curfast.val)
            if curslow == head:
                dummy.next, last = reverse()
            else:
                last.next, last = reverse()

        return dummy.next

        
        








            

