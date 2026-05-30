class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        ln = len(needle)
        start = 0
        end = ln
        while end <= len(haystack):
            if haystack[start:end] == needle:
                return start
            start += 1
            end += 1
        return -1

# sadbutsad
