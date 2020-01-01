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
