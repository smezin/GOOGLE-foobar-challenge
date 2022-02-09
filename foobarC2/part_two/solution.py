
def solution (pegs):
    """
    Using pegs position the method extracts the gaps (between pegs) list and a raw (unchecked)
    value for the first radius. Afterwards we try to fit the gears on the peg, if successful
    the first gear radius is returned as fraction in [a,b] list
    """
    gaps = [(pegs[i+1]-pegs[i]) for i in range(len(pegs)-1)]
    first_gear_r = get_first_gear_r(gaps)
    if fit_gears(gaps, first_gear_r):
        return first_gear_r
    return [-1,-1]

def get_first_gear_r(gaps):
    """
    Method assumes r as first gear radius. The equation that solves the r value for n gaps (between pegs)
         r     g1-r                 g(n-1)
    is  ---- * ----   *    ......  ------------------------------  = 2
        g1-r  g2-(g1-r)            gn-(g(n-1)-(g(n-2)......+/-r))
    When reducing the equation we are left with r/(gn-g(n-1)+g(n-2)....+/-r), hence r is either preceded with + or - depends
    on for even or odd number of gaps. This will be carried in var 'radius_sign'
    Depending on r's signal, the concised equation will be either r = -2*(sum of (gn-g(n-1)+g(n-2)...+/-g1) or
    r = 2/3*(sum of (gn-g(n-1)+g(n-2)...+/-g1) put simply, the sum coefficient will be either -2 (paired with radius_sign = -1)
    or 2/3 (paired with radius_sign = 1)
    method returns first radius as a list of numerator and denominator
    param gaps: list of gaps between pegs
    returns: first gear radius as fraction in [a,b] int list
    """
    radius_coefficient, radius_sign = (-2, -1) if len(gaps)%2 == 0 else (2/3.0, 1)
    first_gear_r = radius_coefficient * radius_sign*(sum(gaps[::2]) - sum(gaps[1::2]))
    if (first_gear_r%3 == 0):
        return [int(first_gear_r), 1]
    return [int(first_gear_r*3), 3]

def fit_gears(gaps, first_gear_r):
    """
    Checking for each gear if it fits the gap and leaving at least size 1 for the next gear.
    On first mismatch the methods return None. On success (all gears fit) returns True
    param gaps: list of gaps between pegs
    param first_gear_r: first gear radius as fraction in [a,b] list
    returns: True if successful, None if else
    """
    r = first_gear_r[0]/first_gear_r[1]
    for i in range(len(gaps)):
        if r >= gaps[i] - 1:
            return 
        r = gaps[i]-r
    return True


print(solution([4,30,50]))
print(solution([0,20,36,50]))