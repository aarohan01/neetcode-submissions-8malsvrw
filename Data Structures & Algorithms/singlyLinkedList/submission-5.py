class ListNode:

    def __init__(self,val,next_node=None):
        self.val = val
        self.next_node = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        
        curr = self.head.next_node
        i = 0
        while curr: 
            if i == index :
                return curr.val
            i += 1
            curr = curr.next_node

        return -1
            

    def insertHead(self, val: int) -> None:
        
        new_node = ListNode(val)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node

        if new_node.next_node == None:
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        
        new_node = ListNode(val)
        self.tail.next_node = new_node
        self.tail = new_node


    def remove(self, index: int) -> bool:
        
        curr = self.head
        i = 0 
    
            
        #Traverse 
        while i < index:
            i += 1
            curr = curr.next_node
            
            
        #Remove
        if curr and curr.next_node:
            if self.tail == curr.next_node:
                self.tail = curr
            curr.next_node = curr.next_node.next_node
            return True
            
        return False



    def getValues(self) -> List[int]:
        
        values = []
        curr = self.head.next_node
        while curr:
            values.append(curr.val)
            curr = curr.next_node
        return values
