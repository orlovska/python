# A digital root is the recursive sum of all the digits in a number.
#
# If n has more than one digit,
# continue reducing in this way until a single-digit number is produced.


def digital_root(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    else:
        n = int(n[0]) + digital_root(int(n[1:]))
        return n


print(digital_root(162))
