# linear space and time complexity
def is_valid(s: str) -> bool:
    stack = []
    brackets = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    data = list(s)
    for x in data:
        if x in brackets:
            stack.append(brackets[x])
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] != x:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

# debug your code below
print(is_valid("()[]"))
print(is_valid("({"))
print(is_valid("({[]()})"))
