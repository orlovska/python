# Your task is to write a function maskify,
# which changes all but the last four characters into '#'.


def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        res = ""
        for i in cc[:-4]:

            res += "#"
        res += cc[-4:]
    return res


print(maskify("4556364607935616"))
print(maskify("64607935616"))
