# Return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        for index in range(len(haystack)):
            if haystack[index] == needle[0]:
                if haystack[index:index+len(needle)] == needle:
                    return index
        return -1