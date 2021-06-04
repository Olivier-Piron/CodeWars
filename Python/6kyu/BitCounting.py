# Bit Counting

def count_bits(n):
    binary = bin(n)[2:]
    cnt = 0
    for i in binary:
        if i == "1": cnt += 1 
    return cnt
