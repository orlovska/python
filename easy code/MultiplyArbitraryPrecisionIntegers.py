def multiply(num1, num2):
    #  multiply([-2,1], [3, 6])
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    # sign = -1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    # num1[0] = 2, num2[0] = 3
    result = [0] * (len(num1) + len(num2))
    # result = [0,0,0,0]
    for i in reversed(range(len(num1))): #(1, 4) i = 1, 0
        for j in reversed(range(len(num2))): #(2, 3, 5, 6) j = 1, 0, 1, 0
            result[i+j +1] += num1[i] * num2[j]   # result - >[0, 0, 0, 6] - > [0, 0, 3, 6] - > [0, 0, 15, 6] -> [0, 7, 5, 6]
            result[i+j] += result[i+j +1] // 10   # result[i+j] = 0, 0, 1 - > [0, 1, 15, 6], 0
            result[i+j + 1] %= 10                 # result -> [0, 0, 0, 6] -> [0, 0, 3, 6] -> [0, 1, 5, 6] -> [0, 7, 5, 6]
   
    non_zero_digit_indexes = (idx for idx, x in enumerate(result) if x != 0)
    #non_zero_digit_indexes = [1,2,3]
    first_non_zero_idx = next(
        non_zero_digit_indexes,
        len(result)
    )
    #first_non_zero_idx = 1
    result = result[first_non_zero_idx:] or [0]
    # result[1:]
    return [sign * result[0]] + result[1:] # result = [-7, 6, 5]

"""
1) result = [0,9,8,7]
> non_zero_digit_indexes = (idx for idx, x in enumerate(result) if x != 0) 
non_zero_digit_indexes = [1,2,3]
> next([1,2,3], 4) = 1
first_non_zero_idx = 1

2) result = [0,0]
non_zero_digit_indexes = []
first_non_zero_idx = next([], 2)
result[first_non_zero_idx:] = result[2:] = []
result = [] or anything = anything


"""