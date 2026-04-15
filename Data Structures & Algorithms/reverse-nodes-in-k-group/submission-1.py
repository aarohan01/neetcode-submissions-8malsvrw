# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        ### Bruteforce ###
        # List of nodes 
        res = []
        cur = head
        while cur:
            res.append(cur)
            cur = cur.next
        
        print([r.val for r in res])

        '''
        L = 0
        R = k 

        while R <= len(res):

            prev = res[R] if R < len(res) else None
            while L < R:
                x = prev.val if prev is not None else None
                print(f'Connected {res[L].val} to {x}')
                res[L].next = prev
                prev = res[L]
                L += 1
            R += k
            
        print([(r.val,r.next.val) for r in res if r.next is not None])
        return res[k-1]
        '''

        '''
        L = 0
        R = k

        # Pass One
        while R <= len(res):

            prev = res[L]
            L += 1

            while L < R:
                res[L].next = prev
                prev = res[L]
                L += 1

            R += k
            
        print([(r.val,r.next.val) for r in res if r.next is not None])

        # Pass Two 
        L = 0
        R = k

        while R <= len(res):
            
            res[L].next = res[R] if R < len(res) else None
            L, R = L + k, R + k

        print([(r.val,r.next.val) for r in res if r.next is not None])
        
        return res[k-1]

        '''

        ### Arrange in the node and then rewire the next 

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
        








            

