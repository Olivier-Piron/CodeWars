# Vasya - Clerk

def tickets(people):
    TwentyFive = 0
    Fifty = 0
    
    for i in people:
        if i == 25:
            TwentyFive += 1
            
        if i == 50:
            TwentyFive -= 1
            if TwentyFive < 0:
                return "NO"
            Fifty += 1
            
        if i == 100:
            if TwentyFive < 3:
                TwentyFive -= 1
                Fifty -= 1
                if TwentyFive < 0 or Fifty < 0:
                    return "NO"
            if TwentyFive > 3:
                TwentyFive -= 3
    return "YES" 
