from collections import deque
INF = float('inf')
UNXPLORED = -1

def solution(entrances, exits, path):
    escape_plan = FluffyEscapism(entrances, exits, path)
    escape_plan.solve()
    return escape_plan.max_bunnies_saved
    
class FluffyEscapism:
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
        self.max_bunnies_saved = 0
        self.graph = []
        self.vertices_n = len(path) + 2
        inner_path_n = len(path)
        virtual_single_source = [INF if i in entrances else 0 for i in range(inner_path_n)] 
        virtual_single_source.append(0)                     #right padding
        virtual_single_source.insert(0,0)                   #left padding
        self.graph.append(virtual_single_source)
        for i in range(inner_path_n):
            padded_path = path[i]
            padded_path.append(INF if i in exits else 0)    #mark as sink if escape pods level
            padded_path.insert(0,0)
            self.graph.append(padded_path)
        self.graph.append([0]*(inner_path_n+2))

    def get_path_bfs(self, root=0):
        """
        Breadth-first Searching for a path from root, hopefully will found paths deep enough to reach the exits
        """
        origins = [UNXPLORED] * (self.vertices_n)
        decendents_q = deque()
        decendents_q.append(root)
        while decendents_q and origins[-1] == UNXPLORED:
            _from = decendents_q.popleft()
            for _to in range(self.vertices_n):
                if self.graph[_from][_to] > 0 and origins[_to] == UNXPLORED: 
                    #has positive path to unvisited vertice
                    decendents_q.append(_to)
                    origins[_to] = _from
        path = []
        vertice = origins[-1]
        while vertice != 0:
            if vertice == UNXPLORED:
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
        self.max_bunnies_saved += edge_max_bunnies
        #fix max bunnies capacity on path
        _from = 0
        for _to in escape_path:
            self.graph[_from][_to] -= edge_max_bunnies # reduce capacity from 'outward' flow
            self.graph[_to][_from] += edge_max_bunnies # increce capaticy the opposite direction
            _from = _to                                # next step

    def solve(self):
        """
        As long as there is a path, pack it with bunnies!
        """
        while True:
            escape_path = self.get_path_bfs()
            if escape_path:
                self.exhaust_escape_path(escape_path)
            else:
                break
