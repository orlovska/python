# Write a method that takes an array of consecutive (increasing) letters as input
# and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.


def find_missing_letter(chars):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chars = "".join(chars)

    test = False
    if chars == chars.upper():
        chars = chars.lower()
        test = True

    n = 0
    indexinAlph = alphabet.find(chars[0])
    while chars[n] == alphabet[indexinAlph]:
        n += 1
        indexinAlph += 1
        continue

    return alphabet[indexinAlph].upper() if test is True else alphabet[indexinAlph]


print(find_missing_letter(["a", "b", "c", "d", "f"]))
print(find_missing_letter(["O", "Q", "R", "S"]))

