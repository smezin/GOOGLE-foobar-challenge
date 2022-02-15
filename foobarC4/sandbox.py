
def solution (times, time_limit):
    """
    1.  Get the number of bunnies
    2.  Set a list of bunnies positions
    3.  create time durations matrix
    4.  In case we detect negative cycle HOORAY! we can make time to save all the bunnies. BUT we only check for possible negative 
            paths starting in our start row, since we can't just spawn anywhere!
    5.  Otherwise, we check for possible picking order, starting with longest possible paths (cause we want to save them all)
            always beginning at start and finishing at bulkhead
    6.  Once path is found (which because of step 5 is equally good, or better, than any other path) it is returned 
    7.  If none found we return an empty list (and best of luck wishes for the running bunnies)
    """
    n_bunnies = len(times) - 2
    bunnies_position = [bunny for bunny in range(1, n_bunnies+1)]
    time_durations_matrix = create_time_durations_matrix(times)

    if update_paths(time_durations_matrix, time_durations_matrix[0], break_on_update=True) == NEG_PATH_DETECTED:
        return list(range(n_bunnies))

    for n_bunnies_to_pick in range (n_bunnies, 0, -1):
        for picking_order in all_perms(bunnies_position, n_bunnies_to_pick):                    # n_bunnies_to_pick goes from most bunnies to least
            path_duration = sum_path_durations(picking_order, time_durations_matrix)            # if path, by given picking order, satifsy time_limit restriction, return it 
            if path_duration <= time_limit:
                return [index - 1 for index in sorted(picking_order)]                          
    return[]
    
def sum_path_durations(picking_order, time_durations_matrix):
    """
    For given picking order (bunnies permutation) sum the times from start to first bunnies,
    then each edge to the following bunny, finally from last bunny to bulkhead
    """
    path_duration = 0
    path_duration += time_durations_matrix[0][picking_order[0]]                                 #starting time to first bunny
    for i in range(1, len(picking_order)):                                                      #picking up bunnies path time
        u = picking_order[i-1] 
        v = picking_order[i]
        path_duration += time_durations_matrix[u][v]
    path_duration += time_durations_matrix[picking_order[-1]][len(time_durations_matrix)-1]     #getting last bunny to bulkhead time
    return path_duration

def create_time_durations_matrix(graph):
    """
    the algorithm initializes the distance to the source to 0 and all other nodes to infinity. 
    Then for all edges, if the distance to the destination can be shortened by taking the edge, 
    the distance is updated to the new lower value. At each iteration i that the edges are scanned, 
    the algorithm finds all shortest paths of at most length i edges (and possibly some paths longer than i edges). 
    Since the longest possible path without a cycle can as many edges as the graph size as represented as adjacency matrix, 
    the edges must be scanned graph len times to ensure the shortest path has been found for all nodes
    """
    durations_matrix = []
    for start_point in range(len(graph)):
        durations_matrix.append(find_distance(graph, start_point))
    return durations_matrix

def find_distance(graph, start_point):
    n = len(graph)
    distance = [float('inf')] * n       #Initialize the distance to all vertices to infinity
    distance[start_point] = 0           #The distance from the start_point to itself is zero
    #for i in range(n):
    distance = update_paths(graph, distance)
    return distance


def update_paths(graph, distance, break_on_update=False):
    n = len(graph)
    for u in range(n):
        for v in range(n):
            weight = graph[u][v]
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                if (break_on_update):
                    return NEG_PATH_DETECTED
    return distance

def all_perms(iterable, r=None):
    """
    As implemented by 'itertools'
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
