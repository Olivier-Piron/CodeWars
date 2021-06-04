# Unique In Order

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    li = []
    for i in iterable:
        if len(li) < 1:
            li.append(i)
        elif len(li) >= 1 and i != li[len(li)-1]:
            li.append(i)
    return li
