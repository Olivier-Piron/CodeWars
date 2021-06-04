# Strip Comments

def solution(string, markers):
    lines = string.split('\n')
    out = ''
    for line in lines:
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        out += line.rstrip(' ')+'\n'
    return out[:-1]