# Last digit of a huge number

# https://www.geeksforgeeks.org/find-last-digit-of-ab-for-large-numbers/

def last_digit(lst):
    size = len(lst)
    if size == 0:
        return 1
    
    last_digit = 1
    for number in lst[::-1]:
        if last_digit == 0:
            last_digit = 1
        elif last_digit == 1:
            last_digit = number
        else:
            last_digit = number**(last_digit%4+4)

    return last_digit%10