# Write a program that multiplies two nonnegative integers. 
# The only operators you are allowed to use are
#  assignment,
#  the bitwise operators >>, <<, |, &, ~, ^ 
#  equality checks and Boolean combinations thereof.
# You may use loops and functions that you write yourself. 
# These constraints i*ply, for example, that you cannot use 
# increment or decrement, or test if r < y.
# Hint: Add using bitwise operations; multiply using shift-and-add.

def multiply(x, y):
 #   multiply(13, 9)  (1101, 1001)
   
    def add(a, b):# (0, 1001) (1001, 100100)  (101101, 1001000)
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b 
        while temp_a or temp_b:#(1, 2, 3, 4) (1, 2, 3, 4, 5, 6) (1, 2, 3, 4, )
            ak, bk = a & k, b & k
            # ak1 = 0, 0, 0, 0
            # bk1 = 1, 0, 0, 1000
            # ak2 = 1, 0, 0, 1000, 0, 0
            # bk2 = 0, 0, 100, 0, 0, 100000
            # ak3 = 1, 0, 100, 1000, 0, 100000, 0
            # bk3 = 0, 0, 0, 1000, 0, 0, 1000000
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin) 
            # carryout1 = 0, 0, 0 
            # carryout2 = 0, 0, 0, 0
            # carryout3 = 0, 0, 0, 1000, 0, 0, 0
            running_sum |= ak ^ bk ^ carryin
            # running_sum1  = 1, 1, 1, 1001
            # running_sum2 = 1, 1, 101, 1101, 1101, 101101
            #  running_sum3 = 1, 1, 101, 101, 10101, 110101, 1110101
            carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
            # k1 = 10, 100, 1000
            # temp_a1 = 0, 0, 0
            # temp_b1 = 100, 10, 1
            # k2 = 10, 100, 1000, 10000, 100000
            # temp_a2 = 100, 10, 1
            # temp_b2 = 10010, 1001, 100, 10, 1, 0
            # carryin3 = 0, 0, 0, 10000, 0, 0, 0
            # k3 = 10, 100, 1000, 10000, 100000, 1000000, 10000000
            # temp_a3 = 10110, 1011, 101, 10, 1, 0, 0
            # temp_b3 = 100100, 10010, 1001, 100, 10, 1, 0
        return running_sum | carryin #1001, 101101, 1110101
    running_sum = 0
    while x: # Examines each bit of x. (1, )
        if x & 1: #(1, 2)
            running_sum = add(running_sum, y)
            # running_sum1 = add(0, 1001) = 1001
            #running_sum2 = add(1000, 100100) = 101101
            #running_sum3 = add(101101, 1001000) = 1110101
        x, y = x >> 1, y << 1  
        # x = 110, 11, 1, 0
        # y = 10010(2 + 16 = 18), 100100, 1001000, 10010000
    return running_sum #1110101