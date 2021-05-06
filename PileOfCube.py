# Build a pile of Cubes

def find_nb(m):
    n = 0
    while (m > 0):
        n += 1
        m -= n**3
    return n if m == 0 else -1
  
# s = (x + x-1 + x-2 + x-3)^3
# s = ((x(x-1))/2)^3
# x^2 + x - 2s^1/3 = 0
    
#Wolfram Alpha solve for x:
# x = (sqrt(8*srt(s)+1)-1)/2

# def find_nb(m):
#     s = int((2*m**0.5)**0.5)
#     if (s*(s+1)/2)**2 == m:
#         return s
#     return -1
