class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.arr = nums
        self.k = k
        print(self.k)

    def add(self, val: int) -> int:

        self.arr.append(val)
        self.arr.sort()
        print(self.arr)
        return self.arr[-self.k]
        
