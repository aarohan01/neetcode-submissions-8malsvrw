### Doubly Linked List ###
# Time: O(1) for operations 
class ListNode: 

    def __init__(self, val, prev=None, next=None):

        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        
        self.head, self.tail = ListNode(-1), ListNode(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
        self.capacity = k
  

    def enQueue(self, value: int) -> bool:

        if self.size >= self.capacity:
            return False
        
        node = ListNode(value)

        prev, next = self.tail.prev, self.tail

        node.next, node.prev = next, prev
        prev.next, next.prev = node, node

        self.size += 1

        return True


    def deQueue(self) -> bool:

        if self.size == 0:
            return False


        node = self.head.next
        node.next.prev = self.head
        self.head.next = node.next

        self.size -= 1

        return True

    def Front(self) -> int:
        if self.size > 0:
            return self.head.next.val
        return -1
        

    def Rear(self) -> int:
        if self.size > 0:
            return self.tail.prev.val
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()