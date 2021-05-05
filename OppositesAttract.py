# Opposites Attract

def lovefunc( flower1, flower2 ):
    return False if flower1%2==flower2%2 else True

###

lovefunc = lambda i,j:(i+j)%2
