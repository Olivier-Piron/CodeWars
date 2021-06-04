# The Millionth Fibonacci Kata

def simple_fib(n):
    n1, n2 = 0, 1
    count = 0
    while count < n:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return n1

def fib(n):
    if n == 0:
        return 0
    elif n < 0:
        n = -n
        if n%2 == 0:
            return -simple_fib(n)
        else:
            return simple_fib(n)
    else:
        v1 = 1  
        v2 = 1
        v3 = 0  
        for rec in bin(n)[3:]: 
            calc = v2*v2
            v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
            if rec=='1':    
                v1, v2, v3 = v1+v2, v1, v2
        return v2