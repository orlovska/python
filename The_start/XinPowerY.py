#Write a program that takes a double x and an integer y and retums x/. 
# You can ignore overflow and underflow.
# Hint: Exploll mathematical properties of exponentiation.


def power(x, y):
    #power(1.1, 8):
    result, power = 1.0, y
    #power = 1000
    if y < 0:
        power, x = -power,1.0/x
    while power:#(1,2,3,4)
        if power & 1: 
            result *= x
            #result = 2,14358881
        x, power = x * x, power >> 1 
        #x = 1,21 ; 1,4641; 2,14358881
        #power = 0100 ; 0010; 0001
    return result