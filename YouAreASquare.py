# You're a square!

import math

def is_square(square):      
    if square < 0: 
        return False
    else:
        n = math.isqrt(square)
        return True if n*n == square else False
