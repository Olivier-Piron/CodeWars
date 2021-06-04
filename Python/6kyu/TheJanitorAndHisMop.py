# Simple Fun #265: The Janitor And His Mop

from string import ascii_lowercase

def the_janitor(word):
    li = []
    for i in range(26):
        li.append(0)
    
    for c in ascii_lowercase:
        first = word.find(c)
        last = word.rfind(c)
        li[ord(c)-97] = last - first + 1 if first != -1 else 0
    return li