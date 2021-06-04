# Replace With Alphabet Position

def alphabet_position(text):
    n = ''
    x = text.lower()
    for i in x:
        if (ord(i) > 96 and ord(i) < 123):
            n += str(ord(i)-96) + " "
    return n.rstrip()