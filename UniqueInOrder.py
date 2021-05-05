# Unique In Order

def unique_in_order(iterable):
    li = []
    for i in iterable:
        if len(li) < 1:
            li.append(i)
        elif len(li) >= 1 and i != li[len(li)-1]:
            li.append(i)
    return li
