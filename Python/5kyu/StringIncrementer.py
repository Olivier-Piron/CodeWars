import re

def increment_string(strng):
    print(strng)
    if len(strng) == 0:
        return '1'
    elif strng == '1':
        return '2'
    i = len(strng)-1
    numbers = ''
    while i > 0:
        if strng[i].isdigit():
            numbers = strng[i] + numbers
        else:
            break
        i -= 1
    text = strng[:i+1]
    
    if len(text) != 0 and len(numbers) == 0:
        zero = '1'
        return f'{text}{zero}'
    
    else:
        zero = str(int(numbers) + 1).zfill(len(numbers))
        return f'{text}{zero}'