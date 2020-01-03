def who_is_next(names, number_in_line):
    # each person in line drink cola and double themselves,
    # if cola_count = 3, then each person drunk 3 cola's,
    # so it's 2*2*2 persons in line for sure
    cola_count = 0

    # whant to know how much cola have they drunk
    # and substract all new groups of doubled people
    while number_in_line > len(names) * 2**cola_count:
        number_in_line -= len(names) * 2**cola_count
        cola_count += 1
    # for next cola_count not everyone from names[] pass
    # want to know how many of them have already got their cola
    index = 0
    index = number_in_line // 2**cola_count

    # can use this number as index for person in the given list
    # cheking if it is the last doubled version of person
    if number_in_line % 2**cola_count == 0:
        return names[index - 1]
    else:
        return names[index]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print((who_is_next(names, 7230702951)))
