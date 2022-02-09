from cmath import pi
from timeit_decorator import timeit_decorator

@timeit_decorator
def reducer (n):
    """
    To solve it we look at n in it's binary representation, where dividing by 2 is not more than chopping the least significant bit IF it 
    equals 0, otherwise we risk a pellet breaking explosion! Since division gets us faster to our goal, whenever it is possible we'll use it.
    When division is too risky we will have to choose between adding and subtracting a single pellet.
    1.  In case our last 2 digits (base 2) are 11 we will add, getting 00 which is better than subtracting and getting 10 since we will earn at least
        two upcoming divisions instead of 1.
    2.  In case our last 2 digits (base 2) are 01 we will subtract, getting 00 which is better than adding and getting 10 since we will earn at least
        two upcoming divisions instead of 1.
    In the edge case where n is last AND ONLY 2 digits (base 2) are 11 (hence n==3), we will subtract 
    """
    pellets = int(n)
    operations = 0
    while pellets != 1:                         #handling *0
        if pellets%2 == 0:
            
            pellets = pellets>>1
        elif pellets != 3 and pellets%4 == 3:   #handling 11, excluding edge case n==3 
            pellets += 1
        else:                                   #handling 01, and edge case n==3            
            pellets -= 1
        operations += 1
    return operations

x = str(int((round(pi,307)) * 10**300))
x = x*10
print('Total running time for', len(x), 'size string')
print('Result:', reducer(x))