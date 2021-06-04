# Build Tower

def tower_builder(n_floors):
    spaces = (n_floors-1)
    
    li = []
    for i in range (n_floors):
        li.append((spaces-i)*' ' + (2*i+1)*'*' + (spaces-i)*' ')
    return li
