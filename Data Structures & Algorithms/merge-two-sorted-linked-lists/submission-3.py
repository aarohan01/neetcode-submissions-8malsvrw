# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ###BruteForce### 
        #convert to list, append, sort the list, reconvert to linkedlist
        #O(n+n) + n*k logkn + O(n*k) 


        ###Solution 1###
        #Intuition - make a dummy node a pointer tail to the dummy node
        #tail tracks the result while l1 and l2 traverse the respective lists
        #While bothe pointers exits, loop throuh and attach using tail pointer 
        #Once any list end in the loop attach the remaining nodes.
        '''
        #Edge case 
        if not list1 :
            return list2
        elif not list2 :
            return list1

        dummy = ListNode()
        tail = dummy

        l1 = list1
        l2 = list2

        #Loop
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else :
                tail.next = l2
                tail = l2
                l2 = l2.next
        
        #Remianing nodes
        while l1:
            tail.next = l1
            tail = l1
            l1 = l1.next
        while l2:
            tail.next = l2
            tail = l2
            l2 = l2.next
        
        return dummy.next
        '''


        ### Solution 1 works but after seeing actual solution, this can be simplified ###
        ### Solution 2 ###
        # One thing that I didn't think : we do not have to traverse the entire linked list 
        # Once a list is finished, i.e don't have to place tail pointer to end. just attach and give dummy.next
        # Another redundancy is the tail pointer movement in while loop that is common, so instead of tail = l1 , tail = l2, tail can just be tail.next

        #Edge case 
        if not list1 :
            return list2
        elif not list2 :
            return list1

        dummy = ListNode()
        tail = dummy

        l1 = list1
        l2 = list2

        #Loop
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else :
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        #Remianing nodes
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        
        return dummy.next


