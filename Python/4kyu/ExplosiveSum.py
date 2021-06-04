# Explosive Sum

def exp_sum(n):
    part = [1] + [0] * n
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            part[j] += part[j - i]
    return part[-1]