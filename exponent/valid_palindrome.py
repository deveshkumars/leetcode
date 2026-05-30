# linear time and constant space
def is_palindrome(s: str) -> bool:
    s = list(filter(lambda x: x.isalnum(), list(s.lower())))
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n-i-1]:
            return False
    return True

# debug your code below
print(is_palindrome('abcba')) # true
print(is_palindrome('abcba7.HH')) # false
print(is_palindrome("H123!@321h")) # true
print(is_palindrome('race a car')) # false
print(is_palindrome('race car')) # true
