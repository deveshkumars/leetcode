# linear soln
def longest_substring_without_repeat(s: str) -> int:
    if s == "":
        return 0
    elif len(s) == 1:
        return 1
    max_len = 0
    chars = {}
    start = 0
    end = 0
    for start in range(len(s)):
        # if applicable, remove old char
        if start != 0:
            chars[s[start - 1]] = False
        
        # increase end as much as possible
        while end < len(s) and (s[end] not in chars or chars[s[end]] == False):
            chars[s[end]] = True
            end += 1

        # update max_len
        if end - start > max_len:
            max_len = end - start
        # print(start, end, chars, max_len)
    return max_len



# debug your code below
print(longest_substring_without_repeat('abcdeffghij')) # 6
print(longest_substring_without_repeat('abcabcbb')) # 3
print(longest_substring_without_repeat('bbbbb')) # 1
print(longest_substring_without_repeat('')) # 0
print(longest_substring_without_repeat('pwwkew')) # 3
