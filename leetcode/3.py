class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_word = []
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        start = 0
        end = 0
        max_len = 0
        while end < len(s):
            print("start", start, "end", end, "current_word", current_word)
            if s[end] in current_word:
                while start < end:
                    if s[start] == s[end]:
                        start += 1
                        current_word.pop(0)
                        break
                    else:
                        start += 1
                        current_word.pop(0)
            
            current_word.append(s[end])

            end += 1   
            max_len = max(max_len, len(current_word))
        return max_len1
