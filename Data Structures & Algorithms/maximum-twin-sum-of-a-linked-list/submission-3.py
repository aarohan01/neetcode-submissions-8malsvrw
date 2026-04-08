# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        ### Bruteforce ###
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
