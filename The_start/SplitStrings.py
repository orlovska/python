# Complete the solution so that it splits the string into pairs of two characters.
#
# If the string contains an odd number of characters then
# it should replace the missing second character of the final pair
# with an underscore ('_').


def solution(s):
    collect = ""
    lst = []
    for m in s:
        collect += m
        if len(collect) == 2:
            lst.append(collect)
            collect = ""
    if len(collect) == 1:
        collect += "_"
        lst.append(collect)
    return lst


print(solution("abc"))
print(solution("abcdef"))
