# Write a function that takes in a string of one or more words,

# and returns the same string, but with all five or more letter words reversed


def spin_words(sentence):
    res = []
    for str1 in sentence.split():
        if len(str1) > 4:
            res.append(str1[::-1])
        else:
            res.append(str1)
    return " ".join(res)


print(spin_words("Hey fellow warriors"))
