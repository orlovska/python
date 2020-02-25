def multiply(num1, num2):
    #  multiply([-2,1], [3])
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    # sign = -1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    # num1[0] = 2, num2[0] = 3
    result = [0] * (len(num1) + len(num2))
    # result = [0,0,0]
    for i in reversed(range(len(num1))): #(1, 2) i = 1, 0
        for j in reversed(range(len(num2))): #(1) j = 0
            result[i+j +1] += num1[i] * num2[j]   # result - >[0, 0, 3] - > [0, 6, 3]
            result[i+j] += result[i+j +1] // 10   # result[i+j] = 0, 0
            result[i+j + 1] %= 10                 # result -> [0, 0, 3] -> [0, 6, 3]
   
    
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    # result[6:]
    return [sign * result[0]] + result[1:] # result = [-6, 3]
