# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        ### Bruteforce solution ###
        # convert linked-list to array, i.e go through each and append in array O(n) time O(n)
        # reverse the array, again O(n) time and either O(1) or O(n) complexity
        # convert again to linked-list O(n) time and O(n) space by traversing the linked list and changing values.
        # So time and space : O(n) 

        # Traverse and convert to list 
        new_list = []
        cur1 = head
        while cur1:
            new_list.append(cur1.val)
            cur1 = cur1.next

        new_list = new_list[::-1]
        #print(new_list)

        # Recreate the linked list
        cur2 = head
        for i in range(len(new_list)):
            cur2.val = new_list[i]
            cur2 = cur2.next
            
        return head
        '''
        '''
        ### Solution 1 ###
        ## Intuition ##
        # Given - structure of listnode object, head as input.
        # Possible type of inputs - empty and one item, multiple items ex : 3
        # Need two pointers  to track and a temporary variable to swap
        # Use one pointer to track previous node , one for current and temporary to 
        # store next node of current. Do this till current node is not None.
        # Complexity : O(n) and O(1) space

        
        cur1 = head
        if head and head.next :
            cur2 = cur1.next
            cur1.next = None
        
            while cur2:
                tmp = cur2.next
                cur2.next = cur1
                cur1 = cur2
                cur2 = tmp
        
            head = cur1

        return head
        
        '''

        ### Solution Final ### After looking solution ###
        ### Solution 1 works perfectly and achives the goal ###
        # How ever it could have been easier, as I had inititally missed one detail,
        # the current head need to point to None.
        # Thus it would be better to have cur1 as None and cur2 as current head and do 
        # the same thing.

        cur1 = None
        cur2 = head

        while cur2:
            tmp = cur2.next 
            cur2.next = cur1
            cur1 = cur2 
            cur2 = tmp
        
        head = cur1
        return head


