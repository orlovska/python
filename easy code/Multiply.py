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
 #   multiply(2, 4)  10, 100
   
    def add(a, b):# (0, 1000)
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b 
        while temp_a or temp_b:#(1,2,3,4)
            ak, bk = a & k, b & k
            # ak = 0, 0, 0, 0
            # bk = 0, 0, 0, 1000
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin) 
            # carryout = 0, 0, 0, 0
            running_sum |= ak ^ bk ^ carryin
            # running_sum  = 0, 0, 0, 1000
            carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
            # k = 10, 100, 1000
            #  temp_a = 0, 0, 0, 0
            # temp_b = 100, 10, 1, 0
        return running_sum | carryin #1000
    running_sum = 0
    while x: # Examines each bit of x. (1, )
        if x & 1: #(1,)
            running_sum = add(running_sum, y)
            # running_sum = add(0, 1000) = 1000
        x, y = x >> 1, y << 1  
        # x = 1, 0
        # y = 1000, 10000
    return running_sum #1000 = 8