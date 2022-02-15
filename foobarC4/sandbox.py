from itertools import permutations


def solution (times, time_limit):
    n_bunnies = len(times) - 2
    bunnies = [bunny for bunny in range(1, n_bunnies+1)]
    distances = bellman_ford(times)
    if negative_cycles(distances):
        return range(n_bunnies)
    for i in range (n_bunnies, 0, -1):
        for perm in permutations(bunnies, i):
            time = get_path_time(perm, distances)
            if time <= time_limit:
                return [index - 1 for index in sorted(perm)]
    return[]
    
def get_path_time(bunnies, graph):
    time = 0
    time += graph[0][bunnies[0]]
    time += graph[bunnies[-1]][len(graph)-1]
    for i in range(1, len(bunnies)):
        u = bunnies[i-1]
        v = bunnies[i]
        time += graph[u][v]
    return time

def bellman_ford(graph):
    distances = []
    for vertex in range(len(graph)):
        distances.append(find_distance(graph, vertex))
    return distances

def find_distance(graph, source):
    n = len(graph)
    distance = [float['inf']] * len(graph)
    distance[source] = 0 #graph[source][source] but diagonal equals 0 
    for i in range(n):
        for u in range(n):
            for v in range(n):
                weight = graph[u][v]
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    return distance

def negative_cycles(graph):
    distance = graph[0] #starting row
    n = len(graph)
    for u in range(n):
        for v in range(n):
            weight = graph[u][v]
            if distance[u] + weight < distance[v]:
                return True
    return False