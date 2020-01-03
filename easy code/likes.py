def likes(names):
    if len(names) == 0:
        name = "no one" + " likes"
    elif len(names) == 1:
        name = names[0] + " likes"
    elif len(names) == 2:
        name = names[0] + " and " + names[1] + " like"
    elif len(names) == 3:
        name = names[0] + ", " + names[1] + " and " + names[2] + " like"
    else:
        name = (
            names[0] + ", " + names[1] + " and " + str(len(names[2:])) + " others like"
        )
    return "{} this".format(name)


print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))

