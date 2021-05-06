# Human Readable Time

def make_readable(seconds):
    hh = seconds//3600
    seconds = seconds - 3600*hh
    if hh < 10:
        hh = '0'+str(hh)
    mm = seconds//60
    ss = seconds - 60*mm
    if mm < 10:
        mm = '0'+str(mm)
    if ss < 10:
        ss = '0'+str(ss)
    return f'{hh}:{mm}:{ss}'
