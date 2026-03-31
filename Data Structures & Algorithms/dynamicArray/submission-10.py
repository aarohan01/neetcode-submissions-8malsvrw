class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:

        if self.capacity == self.size :
            self.resize()
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        
        last_element = self.array[self.size - 1] 
        self.array[self.size - 1] = 0
        self.size -= 1
        return last_element

    def resize(self) -> None:

        self.array = self.array + [0] * self.capacity
        self.capacity = 2 * self.capacity


    def getSize(self) -> int:
        
        return self.size
    
    def getCapacity(self) -> int:

        return self.capacity
