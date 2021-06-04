# Scramblies

def scramble(s1, s2):
    li1 = sorted(s1)
    li2 = sorted(s2)
    
    if li1 == li2:
        return True
    for i in range(97, 123):
        if li1.count(chr(i)) < li2.count(chr(i)):
            return False
    return True
