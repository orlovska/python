# If we list all the natural numbers below 10 that are multiples of 3 or 5,
#  we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_multiples(num1, num2, numbers_below):
    lst = []
    mult = 1 * num1
    while mult < numbers_below:
        for x in range(2, numbers_below):
            mult == x * num1
            lst.append(mult)
    mult = 1 * num2
    while mult < numbers_below:
        for x in range(2, numbers_below):
            mult == x * num2

            if mult not in lst:
                lst.append(mult)
    print(lst)

    return sum(lst)


print(sum_of_multiples(3, 5, 10))

