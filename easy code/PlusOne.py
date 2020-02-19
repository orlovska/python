# Given a non-empty array of digits representing a non-negative integer,
# plus one to the integer.

class Solution(object):
    def plusOne(self, digits):
    
        carry = 1
        while carry == 1:
            digits = digits[::-1]
            for index,value in enumerate(digits):
                print(value)
                
                if value == 9:
                    carry = 1
                    digits[index] = 0 
                    if index == len(digits)-1:
                        
                        digits.append(1)
                        carry = 0
                        break
                else:
                    digits[index] = value+1
                    carry = 0
                    break
        return digits[::-1]