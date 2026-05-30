class Solution:
    def longestPalindrome(self, s: str) -> str:
        history = {}
        ls = len(s)
        best = ""
        for i in range(ls):
            start, end = i, i
            while start >= 0 and end < len(s):
                if s[start] != s[end]:
                    break
                if len(s[start:end+1]) > len(best):
                    best = s[start:end+1]
                start -= 1
                end += 1

        for i in range(ls):
            start, end = i, i+1
            while start >= 0 and end < len(s):
                if s[start] != s[end]:
                    break
                if len(s[start:end+1]) > len(best):
                    best = s[start:end+1]
                start -= 1
                end += 1
        return best



