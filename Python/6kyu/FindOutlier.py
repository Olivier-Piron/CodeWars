# Find The Parity Outlier

def find_outlier(integers):
    i = 0 
    even = 0
    while i < 3:
        if integers[i]%2 == 0:
            even += 1 
        else:
            even -= 1
        i += 1 
    if even > 0:
        for i in integers:
            if i%2 != 0:
                return i
    else:
        for i in integers:
            if i%2 == 0:
                return i
