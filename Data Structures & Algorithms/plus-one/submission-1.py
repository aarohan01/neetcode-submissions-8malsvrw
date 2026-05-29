class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            carry = 1
            for i in range(len(digits)-1,-1,-1):

                if digits[i] == 9 and carry == 1:
                    carry = 1 
                    digits[i] = 0
                else:
                    if carry == 1:
                        digits[i] += carry
                        carry = 0
            if carry == 1:
                return [1] + digits
            else:
                return digits