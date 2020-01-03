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

