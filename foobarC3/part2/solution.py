from sandbox import timeit_decorator

@timeit_decorator
def solution(start, length):
    """
    At the base of this solution stands the bit cancellation propery of the xor operation, which dictates that:
    (4a+0)^(4a+1)^(4a+2)^(4a+3) = 0. The method uses this property to reduce any consecutive sequence of length>3 of integers.
    Doing so assures us that any queue length of consecutive integers will be reduced to be no more than 6 integers long.
    This method calls for xor_reduced_queue for every queue (line) thats is produced by the bunny trainers.
    """
    result = 0
    for i in range (length):
        result ^= xor_reduced_queue(start + i*length, length-i)
    return result

def xor_reduced_queue(start, length):
    """
    The method xor's the reduced queue. The actual reducing is done by ignoring any number sequences that satisfy 
    the pattern (4a+0)^(4a+1)^(4a+2)^(4a+3)
    We xor the first numbers of the queue until we hit the first number that satisfies i%4 == 0 (max of 3 numbers), that our 'head' segment
    Then go to the end of the queue attach it with a 'tail' of numbers, the tails length equal to the total length minus
    the count of numbers at the head of the queue % 4
    """
    queue_xor = 0
    if length < 4:
        #no 4 numbers sequences here...
        for i in range(start, start+length):
            queue_xor ^= i 
    else:
        for i in range(4):
            #xoring the 'head' segment 
            if (start+i)%4:
                queue_xor ^= start+i
                length -= 1
            else:
                break
        tail_len = length%4
        for i in range(tail_len):
            #xoring the 'tail' segment
            queue_xor ^= start+length-1-i
    return queue_xor


print(solution(0,10000))