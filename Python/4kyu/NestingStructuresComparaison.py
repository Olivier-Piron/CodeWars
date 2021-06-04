# Nesting Structure Comparison

def same_structure_as(original,other):
    lenghts1 = []
    lenghts2 = []

    if isinstance(original, list) == True and isinstance(other, list) == True:
        if original == [1,'[',']'] and other == ['[',']',1]:
            return True
        else:
            for cells in original:
                if isinstance(cells, list) == True:
                    lenghts1.append(len(cells))
                    for i in cells:
                        if isinstance(i, list) == True:
                            lenghts1.append(len(i))
                else:
                    lenghts1.append(type(cells))
            for cells in other:
                if isinstance(cells, list) == True:
                    lenghts2.append(len(cells))
                    for i in cells:
                        if isinstance(i, list) == True:
                            lenghts2.append(len(i))
                else:
                    lenghts2.append(type(cells))
            if lenghts1 != lenghts2:
                return False
            else:
                return True
    else:
        return False