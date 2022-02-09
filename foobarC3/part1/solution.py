def solution(n):
    """
    This method implements the Partition Q in order to find (x**bricks) coefficient.
    For doing that the method will construct a list of coefficients where coefficients[2]
    is the coefficient for x**2... and coefficients[n] is the coefficient for x**n.
    Therefore, coefficients[n] is our solution.
    """
    coefficients = [1] + [0]*n
    for ittr in range(1, n):
        new_coefficients = [i for i in coefficients]
        for co_exponent in range (n+1):
            if co_exponent < ittr:
                new_coefficients[co_exponent] = coefficients[co_exponent]
            else:
                new_coefficients[co_exponent] = coefficients[co_exponent] + coefficients[co_exponent - ittr]
        coefficients = [i for i in new_coefficients]
        
    return coefficients[n]
    
# Commander Lambda demanded a schema of steps (marked by height) with no repetition (no two steps are the same height) and
# in descending order. BUT given a list of unique integers we will have only single way to order it by descending order, meaning
# that the task the commander given is the SAME as finding a unique set of numbers the sum to the number of bricks we have, regardless the order.
# Putting it this way, we are facing a Partition Q problem for size n.
# Generating function for Partition Q is (1+i)(1+i**2)(1+i**3).....(1+i**(n+1)) where the coefficient of x**n is the number
# of partitions of sum n.

print(solution(15))