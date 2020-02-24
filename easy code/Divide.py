# Given two positive integers, compute their quotient, 
# using only the addition, subtraction, and shifting operators.
# Hint:Relate x/y to (x - y)/y.

def divide (x , y) :
    # divide(9, 3) (1001, 11)
    result, power = 0, 32 
    y_power = y << power 
    # y_power = 110000000000000000000000000000000...
    while x >= y:
        while y_power > x: #110 < 1001 power = 1
            y_power >>= 1
            # y_power = 11...(31)
            power -= 1
            # power = 31
        result += 1 << power
        # result = 10
        x -= y_power 
        # x  = 1001
        #     -0110
        #      0001
    return result + x
