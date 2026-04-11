# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        ### Bruteforce - Array and Two pointers ###
        # Add the nodes themselves to an array and then change pointers
        '''
        cur = head 
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        
        print(arr)

        L, R = 0, len(arr)-1
        
        while L < R:
            arr[L].next = arr[R]
            L += 1

            if L >= R:
                break 

            arr[R].next = arr[L]
            R -= 1
        
        # Imp : End doesn't have tail None
        arr[L].next = None
        
        '''


        ### Floyds Slow and Fast + Slow and Slow ###
        ## Find mid reverse from mid3, Use a new slow pointers to reorder ##
        ## Use the example given to figure out : [2,4,6,8] ##
        if not head or not head.next:
            return

        curslow, curfast = head, head 

        # Find midpoint
        while curfast and curfast.next:
            curfast = curfast.next.next
            curslow = curslow.next
        
        #print(curslow.val)
        #print(curfast.val)

        # Reverse from mid
        # Structure : [2,4,6,8] : 2->4->6->None<-6<-8
        prev = None
        while curslow:
            temp = curslow.next
            curslow.next = prev
            prev = curslow
            curslow = temp
        
        
        # Reconstruct the linked list
        newslow, curslow = head, prev
        while curslow.next:

            tmp1 = newslow.next
            newslow.next = curslow
            newslow = tmp1

            tmp2 = curslow.next 
            curslow.next = newslow
            curslow = tmp2
        
            
            





