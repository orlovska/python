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

    return alphabet[indexinAlph].upper() if test == True else alphabet[indexinAlph]

