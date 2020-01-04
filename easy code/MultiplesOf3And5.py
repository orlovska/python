# If we list all the natural numbers below 10 that are multiples of 3 or 5,
#  we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_multiples(num1, num2, numbers_below):
    lst = []
    for x in range(1, numbers_below // num1 + 1):
        if x * num1 < numbers_below:
            lst.append(x * num1)
    for x1 in range(1, numbers_below // num1 + 1):
        if num2 * x1 not in lst and num2 * x1 < numbers_below:
            lst.append(x1 * num2)
    return sum(lst)


print(sum_of_multiples(3, 5, 10))
print(sum_of_multiples(3, 5, 1000))
