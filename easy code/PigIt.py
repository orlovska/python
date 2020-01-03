# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word.
# Leave punctuation marks untouched.


def pig_it(text):
    lst = []
    for x in text.split(" "):
        if x.isalpha():
            lst.append(x[1 : len(x) + 1] + x[0] + "ay")
        else:
            lst.append(x)
    return " ".join(lst)


print(pig_it("Pig latin is cool"))

