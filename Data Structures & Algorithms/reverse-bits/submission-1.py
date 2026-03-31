class Solution:
    def reverseBits(self, n: int) -> int:
        
        ### Bit Manipulation ###
        res = 0
        for i in range(32):
            # Extract last bit 32 times 
            bit = (n >> i) & 1
            print(bit)
            # Right shift the bit in reverse
            res += (bit << (31 - i))
        return res



