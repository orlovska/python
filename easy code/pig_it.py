def pig_it(text):
    lst = []
    for x in text.split(" "):
        if x == "?" or x == "!":
            lst.append(x)
        else:
            lst.append(x[1 : len(x) + 1] + x[0] + "ay")
    return " ".join(lst)

