# Detect Pangram

def check(seq):
    seen = set()
    seen_add = seen.add
    sorted = [x for x in seq if not (x in seen or seen_add(x))]
    return True if sorted == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] else False

def is_pangram(s):
    arr = []
    for i in s:
        if i.isalpha():
            arr.append(i.lower())
    sorted_arr = sorted(arr)
    return True if check(sorted_arr) == True else False