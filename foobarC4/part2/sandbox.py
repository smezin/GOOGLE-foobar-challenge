from collections import deque
INF = float('inf')


def add_source_and_sink(entrances, exits, path):
    """
    The way we get the path creates few 'special' rows, the ones that indicate entrances and exits. 
    This data formatting prevents the solution from treating each row the same. 
    Adding a "virtual parent target", before the source, which is able to supply each entrance with endless bunnies, and
    "virtual sink" which is able to obsorbe endless flow of bunnies from the exit levels will let us
    treat each of the vertices as 'Intermediate room'.
    For that matter the method will take the original graph and add target and sink levels with the corresponding
    source provider and sink obsorber. We will create and return it
    """
    inner_path_n = len(path)
    graph = []
    virtual_single_source = [0, *[INF if i in entrances else 0 for i in range(inner_path_n)], 0] 
    graph.append(virtual_single_source)
    for i in range(inner_path_n):
        graph.append([0, *path[i], INF if i in exits else 0])
    
    return graph

class EscapePods:
    def __init__(self, entrances, exits, path):
        n = len(path)
        m = n + 2

        # graph[0] is the new single source s
        # graph[-1] is the new single sink t
        self.graph = []
        self.size = m
        # for i in range(m):
        #     self.graph.append([0] * m)

        # for i in range(n):
        #     for j in range(n):
        #         self.graph[i+1][j+1] = path[i][j]

        # for num in entrances:
        #     self.graph[0][num + 1] = INF

        # for num in exits:
        #     self.graph[num + 1][m - 1] = INF

    def bfs(self):
        parents = [-1] * self.size
        queue = deque()
        queue.append(0)
        # for i in range(len(self.graph)-1):
        #    print(self.graph[i])
        while queue and parents[-1] == -1:
            u = queue.popleft()
            for v in range(self.size):
                if self.graph[u][v] > 0 and parents[v] == -1:
                    queue.append(v)
                    parents[v] = u
        path = []
        u = parents[-1]
        while u != 0:
            if u == -1:
                return None
            path.append(u)
            u = parents[u]
            #print('path->', path)
        path.reverse()
        #print('path->', path)
        return path

    def solve(self):
        max_flow = 0
        path = self.bfs()

        while path:
            cap = INF
            u = 0
            for v in path:
                cap = min(cap, self.graph[u][v])
                u = v
            max_flow += cap
            u = 0
            for v in path:
                self.graph[u][v] -= cap
                self.graph[v][u] += cap
                u = v
            path = self.bfs()
        return max_flow


def solution(entrances, exits, path):
    escape_pods = EscapePods(entrances, exits, path)
    escape_pods.graph = add_source_and_sink(entrances, exits, path)
    for i in range(len(escape_pods.graph)):
       print(escape_pods.graph[i])
    res = escape_pods.solve()
    return res

#print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 6], [9, 0, 0, 0]]))
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
x = add_source_and_sink([0, 1], [4, 5],[[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
for i in range(len(x)):
    print(x[i])