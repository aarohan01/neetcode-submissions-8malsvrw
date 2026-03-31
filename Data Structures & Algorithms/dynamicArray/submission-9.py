class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n 
        self.length += 1

    def popback(self) -> int:
        
        last = self.arr[self.length -1]
        self.arr[self.length -1] = 0
        self.length -= 1
        return last

    def resize(self) -> None:
        
        new_arr = self.arr[:] + [0]*self.capacity
        self.capacity = 2*self.capacity
        self.arr = new_arr 


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
