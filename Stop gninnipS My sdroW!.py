def spin_words(sentence):
    res = []
    for str1 in sentence.split():
        if len(str1) > 4:
            res.append(str1[::-1])
        else:
            res.append(str1)
    return " ".join(res)


print(spin_words("Hey fellow warriors"))
