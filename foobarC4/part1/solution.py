def solution(times, times_limit):
    """
    Based on Bellman-Ford with few 'tweeks', modifying it's ability to find shortest path for finding 
    longest path (most bunnies picked) that satisfies times_limit restriction, simply put, we are looking 
    for a path that is long but quick!
    1.  Get the number of bunnies
    2.  Set a list of bunnies positions
    3.  create time durations matrix
    4.  In case we detect negative cycle HOORAY! we can make time to save all the bunnies. 
    5.  Otherwise, we check for possible picking order, starting with longest possible paths (cause we want to save them all)
            always beginning at start and finishing at bulkhead
    6.  Once a satisfying path is found (which because of step 5 is best possible path) it is returned 
    7.  If none found we return an empty list (and best of luck wishes for the running bunnies)
    """
    n_bunnies = len(times) - 2
    bunnies_position = [bunny for bunny in range(1, n_bunnies+1)]
    times_matrix = create_times_matrix(times)
    #trying to improve paths after all path times checked, if succeeded there is a negative path available
    if update_times(times_matrix, times_matrix[0], break_on_update=True) == NEG_PATH_DETECTED:
        return list(range(n_bunnies))

    for n_bunnies_to_pick in range (n_bunnies, 0, -1):
        for picking_order in permutations(bunnies_position, n_bunnies_to_pick):     # n_bunnies_to_pick goes from most bunnies to least
            path_time = sum_path_times(picking_order, times_matrix)         # if path, by given picking order, satifsy time_limit restriction, return it 
            if path_time <= times_limit:
                return [index - 1 for index in sorted(picking_order)]                          
    return []
    
def create_times_matrix(adjacency_matrix):
    """
    relaxing times (edges) repeatedly for adjacency_matrix * number or rows
    """
    times_matrix = []
    for start_point in range(len(adjacency_matrix)):                         # num of rows, NOT nodes
        times_matrix.append(relax_times(adjacency_matrix, start_point))
    return times_matrix

def relax_times(adjacency_matrix, start_point):
    """
    initializes the duration to the source to 0 and all other nodes to infinity. 
    Then for all edges, if the duration to the destination can be shortened by taking the edge, 
    the duration is updated to the new lower value.
    """
    v = len(adjacency_matrix)
    times = [float('inf')] * v       #Initialize the duration to all vertices to infinity
    times[start_point] = 0           #The duration from the start_point to itself is zero
    for i in range(v-1):
        times = update_times(adjacency_matrix, times)
    return times

def update_times(adjacency_matrix, times, break_on_update=False):
    """
    Bellman-Ford core algorithm, time to each vertex is always an overestimate of the true distance, 
    and is replaced by the minimum of its old value and the length of a newly found path.
    This method also uses to detect negative timed path.
    """
    n = len(adjacency_matrix)
    for u in range(n):
        for v in range(n):
            weight = adjacency_matrix[u][v]
            if times[u] + weight < times[v]:
                times[v] = times[u] + weight
                if (break_on_update):
                    return NEG_PATH_DETECTED
    return times

def sum_path_times(picking_order, times_matrix):
    """
    For a given picking order (bunnies permutation) sum the times from start to first bunnies,
    then each edge to the following bunny, finally from last bunny to bulkhead
    """
    path_time = 0
    path_time += times_matrix[0][picking_order[0]]                                 #starting time to first bunny
    for i in range(1, len(picking_order)):                                                      #picking up bunnies path time
        u = picking_order[i-1] 
        v = picking_order[i]
        path_time += times_matrix[u][v]
    path_time += times_matrix[picking_order[-1]][len(times_matrix)-1]     #getting last bunny to bulkhead time
    return path_time

def permutations(iterable, r=None):
    """
    As implemented by 'itertools'.
    The default implementation yields permutations starting with first (lower) of iterable list,
    hence satisfy the restriction 'If there are multiple sets of bunnies of the same size, 
    return the set of bunnies with the lowest worker IDs (as indexes)' by default checks order
    """
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

NEG_PATH_DETECTED = 'negative path detected'

print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
print(solution([[0, -11, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
