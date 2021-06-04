# Tank Truck

# https://www.mathsisfun.com/geometry/cylinder-horizontal-volume.html
import math

def tankvol(h, d, vt):
    r = d/2
    term1 = math.acos((r-h)/r)
    term2 = (r**2)
    term3 = (r-h)
    term4 = math.sqrt((2*r*h)-(h**2))
    area = (term1*term2)-(term3*term4)
    print("area=", str(area))
    
    length = vt / (math.pi*r**2)
    print("area=", str(length))
    
    return math.floor(area*length)