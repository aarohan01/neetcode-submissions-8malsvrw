class Node:

    def __init__(self,val,next_node=None,prev_node=None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node



class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def isEmpty(self) -> bool:
        
        if self.head.next_node == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        
        new_node = Node(value)
        new_node.prev_node = self.tail.prev_node
        new_node.next_node = self.tail
        self.tail.prev_node.next_node = new_node
        self.tail.prev_node = new_node

        

    def appendleft(self, value: int) -> None:
        
        new_node = Node(value)
        new_node.next_node = self.head.next_node
        new_node.prev_node = self.head
        self.head.next_node.prev_node = new_node
        self.head.next_node = new_node


    def pop(self) -> int:
        
        ### If queue not empty
        if self.head.next_node != self.tail:

            ###Pointer for easy operations
            curr = self.tail.prev_node
            value = curr.val
            self.tail.prev_node = curr.prev_node
            curr.prev_node.next_node = self.tail
            
            return value
        return -1

    def popleft(self) -> int:
        
         ### If queue not empty
        if self.head.next_node != self.tail:

            ###Pointer for easy operations
            curr = self.head.next_node
            value = curr.val
            self.head.next_node = curr.next_node
            curr.next_node.prev_node = self.head
            
            return value
        return -1       
        
