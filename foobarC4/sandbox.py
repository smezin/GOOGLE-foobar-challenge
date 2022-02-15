from distutils.log import ERROR
from itertools import permutations

def solution (times, time_limit):
    """
    1. Get the number of bunnies
    2. Set a list of bunnies id's
    3. Invoke bellman-ford of times adjacency matrix
    4. In case we detect negative cycle HOORAY! we can make time to save all the bunnies 
    5. Otherwise, we check for possible path, starting with longest possible paths (cause we want to save them all) 
    6. Once path is found (which because of step 5 is equally good, or better, than any other path) it is returned 
    7. If none found we return an empty list (and best of luck wishes for the running bunnies)
    """
    # n of bunnies equals n of times minus start and bulkhead
    n_bunnies = len(times) - 2
    bunnies = [bunny for bunny in range(1, n_bunnies+1)]
    distances = bellman_ford(times)
    if update_distance(distances, distances[0], break_on_update=True) == NEG_PATH_DETECTED:
        print('neg')
        return list(range(n_bunnies))
    for i in range (n_bunnies, 0, -1):
        for perm in all_perms(bunnies, i):
            # i goes from longest paths to shortest
            time = get_path_time(perm, distances)
            if time <= time_limit:
                return [index - 1 for index in sorted(perm)]
    return[]
    
def get_path_time(bunnies, graph):
    time = 0
    time += graph[0][bunnies[0]] #starting time
    time += graph[bunnies[-1]][len(graph)-1] #transition to bulkhead time
    for i in range(1, len(bunnies)):
        #path time
        u = bunnies[i-1]
        v = bunnies[i]
        time += graph[u][v]
    return time

def bellman_ford(graph):
    """
    the algorithm initializes the distance to the source to 0 and all other nodes to infinity. 
    Then for all edges, if the distance to the destination can be shortened by taking the edge, 
    the distance is updated to the new lower value. At each iteration i that the edges are scanned, 
    the algorithm finds all shortest paths of at most length i edges (and possibly some paths longer than i edges). 
    Since the longest possible path without a cycle can as many edges as the graph size as represented as adjacency matrix, 
    the edges must be scanned graph len times to ensure the shortest path has been found for all nodes
    """
    distances = []
    for vertex in range(len(graph)):
        distances.append(find_distance(graph, vertex))
    return distances

def find_distance(graph, source):
    n = len(graph)
    distance = [float('inf')] * n       #Initialize the distance to all vertices to infinity
    distance[source] = 0                #The distance from the source to itself is, of course, zero
    #for i in range(n):
    distance = update_distance(graph, distance)
    
    return distance

# def negative_cycles(graph):
#     distance = graph[0] #starting row
#     n = len(graph)
#     for u in range(n):
#         for v in range(n):
#             weight = graph[u][v]
#             if distance[u] + weight < distance[v]:
#                 return True
#     return False

def update_distance(graph, distance, break_on_update=False):
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
