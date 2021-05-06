# Detect Pangram

def is_pangram(s):
    li = []
    x = s.lower()
    for i in x:
        if ord(i) > 96 and ord(i) < 123:
            li.append(i)
    return list(dict.fromkeys(sorted(li))) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
