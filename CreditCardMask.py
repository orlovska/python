def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        res = ""
        for i in cc[:-4]:

            res += "#"
        res += cc[-4:]
    return res

