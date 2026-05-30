from typing import List, Tuple

def str_val(txt) -> int:
    return (sum([ord(x) for x in txt]))

def most_common_words(text: str) -> List[Tuple[str, int]]:
    text = list(text.lower())
    new_text = []
    for x in text:
         if x.isalnum() or x == " ":
            new_text.append(x)
    text = "".join(new_text).split()
    hashmap = {}
    for x in text:
        if x in hashmap:
            hashmap[x] += 1
        else:
            hashmap[x] = 1
    output = []
    for x in hashmap:
        output.append((x, hashmap[x]))
    return sorted(output, key=lambda x: (-x[1], x[0]), reverse=False)

# debug your code below
print(most_common_words("It was the best of times, it was the worst of times."))
