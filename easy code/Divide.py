# Given two positive integers, compute their quotient, 
# using only the addition, subtraction, and shifting operators.
# Hint:Relate x/y to (x - y)/y.

def divide (x , y) :
    # divide(9, 3) (1001, 11)
    result, power = 0, 32 
    y_power = y << power 
    # y_power = 110000000000000000000000000000000...
    while x >= y: # 1001 > 11, 11 = 11
        while y_power > x: # 1 (1100000000...> 1001) 
            #                110 < 1001  with power = 1; 
            #                2 (110 > 11)
            #                 11 !< 11 with power = 0
            y_power >>= 1
            # y_power1 = 11...(31)
            # y_power2 = 11
            power -= 1
            # power1 = 31
            # power2 = 0
        print(power)
        result += 1 << power
        print(result)
        # result = 10, 11
        x -= y_power 
        print(x)
        # x  = 1001
        #     -0110
        #      0011
    return result 


print(divide(9,3))