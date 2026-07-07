# linear solm
def identify_adjacent(s: str, k: int) -> str:
    stack = []
    for x in s:
        if len(stack) == 0:
            stack.append((x, 1))
        else:
            if stack[-1][0] == x:
                if stack[-1][1] + 1 == k:
                    stack.pop()
                else:
                    stack[-1] = (x, stack[-1][1] + 1)
            else:
                stack.append((x, 1))
    
    result = []
    for x in stack:
        for i in range(x[1]):
            result.append(x[0])
    return "".join(result)

# another linear soln 5/31/2026
def identify_adjacent(s: str, k: int) -> str:
    stack = []
    for char in list(s):
        if not stack or stack[-1][0] != char:
            stack.append([char, 1])
        else:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
    outputstr = ""
    for item in stack:
        outputstr += item[0] * item[1]
    return outputstr

# another inefficient soln 5/31/2026
def identify_adjacent(s: str, k: int) -> str:
    s = list(s)
    stop = False
    while not stop:
        stop = True
        lastchar, lastcharcount = "", 0
        for idx, char in enumerate(s):
            if char == lastchar:
                lastcharcount += 1
                if lastcharcount == k:
                    s = s[:idx-k+1] + s[idx+1:]
                    stop = False
                    break
            else:
                lastchar = char
                lastcharcount = 1               
    
    return "".join(s)

# inefficient soln
# def identify_adjacent(s: str, k: int) -> str:
#     s = list(s)
#     if k == 1:
#         return ""
#     elif len(s) <= 1:
#         return s
#     pop_list = []
#     done = False
#     while not done:
#         done = True
#         start = 0
#         end = start + k
#         while end < len(s) + 1:
#             if is_same(s[start:end]):
#                 if len(s) > end:
#                     s = s[:start] + s[end:]
#                 else:
#                     s = s[:start]
#                 start = end + 1
#                 end = start + k
#                 done = False
#                 #print(s)
#             else:
#                 start += 1
#                 end += 1
#     return "".join(s)

def is_same(aloa) -> bool:
    if len(aloa) <= 1:
        return True
    x = aloa[0]
    for i in range(1, len(aloa)):
        if aloa[i] != x:
            return False
    return True

# debug your code below
print(identify_adjacent("abcd", 2)) # 'abcd
print(identify_adjacent("deeedbbcccbdaa", 3)) # aa
print(identify_adjacent("pbbcggttciiippooaais", 2)) # ps
print(identify_adjacent("aaabbbacd", 3)) # 'acd'
