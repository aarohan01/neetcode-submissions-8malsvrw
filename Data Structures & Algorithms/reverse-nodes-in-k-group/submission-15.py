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
        

        '''
        ### Inplace One pass ###
        # This works but cleaner below #

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

            ### Count k nodes, curfast is at k+1
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

        '''

        ### Onepass inplace ###
        # Use a dummy node to start
        # Groupprev and Groupnext keep track of nodes before and after group, groupprev starts at dummy
        # Curslow and Curfast are used to reverse, curfast it at kth node, curslow is at start of group 
        # After moving curfast to kth node, set groupnext
        # Reverse the group keeping in mind to attach the first curslow to groupnext
        # Then after the loop attach groupprev to first node that becomes last
        # Reset curfast to groupprev
        # Time: O(n)
        # Space: O(1)

        dummy = ListNode()
        dummy.next = head
        curfast, curslow = dummy, dummy.next
        groupprev = dummy

        while curfast:

            ### Count k nodes, curfast is at k
            nodecount = 0
            while nodecount != k:
                
                curfast = curfast.next
                nodecount += 1
                if curfast is None:
                    return dummy.next

            print(curfast.val if curfast else None)
            ### Reverse Group
            # Do while loop
            groupnext = curfast.next
            prev = groupnext
            last_when_reversed = curslow
            while curslow != groupnext:
                tmp = curslow.next 
                curslow.next = prev
                #pval = prev.val if prev else None
                #print(f'Connected {curslow.val} to {pval}')
                prev = curslow
                curslow = tmp


            groupprev.next = prev
            groupprev = last_when_reversed
            curfast = groupprev

        
        return dummy.next
            

            


        








            

