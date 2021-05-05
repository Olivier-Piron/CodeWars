# Take a Ten Minute Walk

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        nN = 0
        nS = 0
        nW = 0
        nE = 0
        for i in walk:
            if i == "n": nN += 1 
            if i == "s": nS += 1 
            if i == "w": nW += 1 
            if i == "e": nE += 1
        return True if nN == nS and nW == nE else False
