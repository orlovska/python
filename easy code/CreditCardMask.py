# function maskify,
# which changes all but the last four characters into '#'.


def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        res = ""
        res += "#" * len(cc[:-4])
        res += cc[-4:]
    return res


print(maskify("4556364607935616"))
print(maskify("64607935616"))
