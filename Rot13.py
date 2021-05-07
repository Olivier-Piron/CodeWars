# Rot13

def rot13(message):
    ciphed = ''
    
    for i in message: 
        
        if ord(i) > 96 and ord(i) < 110:
            n = ord(i) + 13
            ciphed += chr(n)
        elif ord(i) > 109 and ord(i) < 123:
            n = ord(i) - 13
            ciphed += chr(n)
            
        elif ord(i) > 64 and ord(i) < 78:
            n = ord(i) + 13
            ciphed += chr(n)
        elif ord(i) > 77 and ord(i) < 91:
            n = ord(i) - 13
            ciphed += chr(n)
        else:
            ciphed += i

    return ciphed
