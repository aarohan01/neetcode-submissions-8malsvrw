# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        ### Bruteforce ###
        # Time : O(n)
        # Space : O(n)
        '''
        arr = []
        cur =  head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        print([x for x in arr])
        maxsum = 0
        L, R = 0, len(arr)-1
        while L <= R:

            maxsum = max(maxsum, arr[L] + arr[R])
            L += 1
            R -= 1
        return maxsum
        '''




        ### Fast and Slow pointers + Reverse the linked list ###

        ### Finding Mid ###
        curfast, curslow = head, head
        prevcurslow = None
        while curfast and curfast.next:
            
            curfast = curfast.next.next
            prevcurslow = curslow
            curslow = curslow.next
            
        prevcurslow.next = None

        print(prevcurslow.val)
        print(curslow.val)


        ### Reversing from Mid ###
        prevcurslow = None
        while curslow:
            tmp = curslow.next
            curslow.next = prevcurslow
            prevcurslow = curslow
            curslow = tmp
        
        #print(prevcurslow.val)
        #print(curslow.val)

        ### Two Pointer on Linked List ###
        newcurslow = head
        curslow = prevcurslow
        maxsum = 0
        while newcurslow and curslow:
            
            maxsum = max(maxsum, newcurslow.val + curslow.val)
            newcurslow, curslow = newcurslow.next, curslow.next

        return maxsum



