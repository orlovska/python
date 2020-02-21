#The parity of a binary word is 1 if the number of 1s 
# in the word is odd; otherwise, it is 0. 
# For example, the parity of 1011 is 1, 
# and the parity of 10001000 is 0. 
# Parity checks are used to detect single bit 
# errors in data storage and communication. 
# It is fairly straightforward to write code 
# that computes the parity of a single 64-bit word.


def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x- 1
    return result 


def count_bits(x): 
    num_bits = 0
    while x: 
        num_bits += x&1 
        print(x)
        x>>=1
        print(x)
    return num_bits


print(count_bits(0b11001))
# 100b = 4
# a)100b - 1b  = 011b (4 - 1 = 3)
# b)100b - 10b = 010b (4 - 2 = 2)
#   -10b
#   010b
