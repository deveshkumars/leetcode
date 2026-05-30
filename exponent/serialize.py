def encode(x: int) -> str:
    return chr(x)

def decode(x: str) -> int:
    return ord(x)

def serialize(l):
    l = [str(encode(len(x))) + x for x in l]
    return str("".join(l))
    
def deserialize(s):
    words = []
    s = list(s)
    i = 0
    while i < len(s) - 1:
        end_index = int(decode(s[i]))
        words.append("".join(s[i+1:i+end_index+1]))
        i += end_index + 1
    return words
# debug your code below
lst = ['hello', 'world']
serialized = serialize(lst)
print("Serialized output:", serialized)

deserialized = deserialize(serialized)
print("Deserialized output:", deserialized)

