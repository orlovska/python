# Given a non-empty array of digits representing a non-negative integer,
# plus one to the integer.

class Solution(object):
    def plusOne(self, digits):
    
    
        digits = digits[::-1]
        digits[0] += 1
     
        for index,value in enumerate(digits):
            
            if value != 10:
                break
            
            digits[index] = 0 
            if index == len(digits)-1:
                digits.append(1)
                break
            digits[index + 1] += 1 
            
        return digits[::-1]
        