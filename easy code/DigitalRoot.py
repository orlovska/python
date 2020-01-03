# A digital root is the recursive sum of all the digits in a number.
#
# If n has more than one digit,
# continue reducing in this way until a single-digit number is produced.


def digital_root(n):
    num = str(n)
    while len(num) > 1:
        summ = []
        for count in range(len(num)):
            summ.append(num[count])
        collect = 0
        for number in summ:
            collect += int(number)
        num = ""
        num += str(collect)
    return int(num)


print(digital_root(16))

