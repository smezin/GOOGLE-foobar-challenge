
def solution (pegs):
    """
    
    """
    gaps = get_gaps(pegs)
    first_radius = get_first_radius(gaps)
    radiuses = get_radiuses(gaps, first_radius)
    if validate_radiuses(radiuses, gaps):
        return first_radius
        #return [int(r[0]), int(r[1])] #p2.7
    return [-1,-1]

def get_gaps(pegs):
    return [(pegs[i+1]-pegs[i]) for i in range(len(pegs)-1)]

def get_first_radius(gaps):
    radius_coefficient, radius_sign = (-2, -1) if len(gaps)%2 == 0 else (2/3.0, 1)
    first_radius_dec = radius_coefficient * radius_sign*(sum(gaps[::2]) - sum(gaps[1::2]))
    if (first_radius_dec%3 == 0):
        return [first_radius_dec, 1]
    return [first_radius_dec*3, 3]

def get_radiuses(gaps, first_radius):
    radiuses = [first_radius[0]/first_radius[1]]
    r = first_radius[0]/first_radius[1]
    for i in range(len(gaps)):
        r = gaps[i]-r
        radiuses.append(r)
    return radiuses

def validate_radiuses(radiuses, gaps):
    for i in range(len(gaps)):
        if (radiuses[i]<1 or radiuses[i]>=gaps[i]):
            return False
    return True

print(solution([4,30,50]))
print(solution([0,20,36,50]))