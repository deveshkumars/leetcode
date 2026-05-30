

def longest_palindromic_substring(s: str) -> str:

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(st) and st[left] == st[right]:
            left -= 1
            right += 1
        return st[left + 1:right]

    start_index = 0
    end_index = 0
    if s == "":
        return ""
    s = list(s)
    st = ['|']
    for x in list(s):
        st.append(x)
        st.append("|")


    longest = ""
    for i in range(len(st)):
        pal = expand_around_center(i, i)
        if len(pal) > len(longest):
            longest = pal   
    return "".join(list(filter(lambda x: x!='|', longest)))

# debug your code below
print(longest_palindromic_substring('raccabrn'))
print(longest_palindromic_substring('level'))
print(longest_palindromic_substring('lvlrraceecarrlebron'))
