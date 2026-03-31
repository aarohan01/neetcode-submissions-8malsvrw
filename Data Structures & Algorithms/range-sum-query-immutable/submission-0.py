class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
        print(f'prefix sum array : {self.prefix}')
        print('Every node in prefix stores sum from index 0 to that index')
        

    def sumRange(self, left: int, right: int) -> int:

        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]
        



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)