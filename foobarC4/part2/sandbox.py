from collections import deque
INF = float('inf')

class EscapePods:
    def __init__(self, entrances, exits, path):
        """
        Creating single source graph and mark exits with infinite out flow.
        The way we get the path creates few 'special' rows, the ones that indicate entrances, more than a single
        entrance will complicate path traversing. Adding a "virtual parent source" allows us to convert the path to a single source path.
        as for the exit(s) row(s), we couldn't care less for it's values since no sane bunny will run away from an infinite 
        selection of escape pods, but we will mark it as infinite outgoing capacity.
        For that matter the method will take the original graph and add "virtual" source vertice with the marking of
        the sink vertice(s)
        """
        self.max_bunnies = 0
        self.graph = []
        self.vertices_n = len(path) + 2
        inner_path_n = len(path)
        virtual_single_source = [0, *[INF if i in entrances else 0 for i in range(inner_path_n)], 0] 
        self.graph.append(virtual_single_source)
        for i in range(inner_path_n):
            self.graph.append([0, *path[i], INF if i in exits else 0])
        self.graph.append([0]*(inner_path_n+2))

    def get_path_bfs(self, root=0):
        """
        Breadth-first Searching for a path from root, hopefully will found paths deep enough to reach the exits
        """
        origins = [-1] * (self.vertices_n)
        decendents_q = deque()
        decendents_q.append(root)
        while decendents_q and origins[-1] == -1:
            _from = decendents_q.popleft()
            for _to in range(self.vertices_n):
                if self.graph[_from][_to] > 0 and origins[_to] == -1: 
                    #has positive path to unvisited vertice
                    decendents_q.append(_to)
                    origins[_to] = _from
        path = []
        vertice = origins[-1]
        while vertice != 0:
            if vertice == -1:
                return None
            path.insert(0, vertice)
            vertice = origins[vertice]
        return path
    
    def exhaust_escape_path(self, escape_path):
        """
        Step 1: accumulate max bunnies for path into self var max_bunnies
        Step 2: fix residual max flow for edges on eascape path
        """
        #accumulate max bunnies for path
        _from = 0
        edge_max_bunnies = INF
        for _to in escape_path:
            edge_max_bunnies = min(edge_max_bunnies, self.graph[_from][_to])
            _from = _to
        self.max_bunnies += edge_max_bunnies
        #fix max bunnies flow on path
        _from = 0
        for _to in escape_path:
            self.graph[_from][_to] -= edge_max_bunnies # reduce capacity from 'outward' flow
            self.graph[_to][_from] += edge_max_bunnies # increce capaticy the opposite direction
            _from = _to                                # next step

    def solve(self):
        while True:
            escape_path = self.get_path_bfs()
            if escape_path:
                self.exhaust_escape_path(escape_path)
            else:
                break

def solution(entrances, exits, path):
    escape_pods = EscapePods(entrances, exits, path)
    for i in range(len(escape_pods.graph)):
       print(escape_pods.graph[i])
    escape_pods.solve()
    return escape_pods.max_bunnies

print(solution([0], [3], [[0, 3, 0, 0], [0, 0, 5, 0], [0, 0, 0, 2], [9, 0, 0, 0]]))
#print(solution([0], [5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# x = add_source_and_sink([0, 1], [4, 5],[[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# for i in range(len(x)):
#     print(x[i])

