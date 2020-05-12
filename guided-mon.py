# Node/Verts/Vertexes/Vertices

# Edges

# Directed Graphs

# Undirected Graphs

# Cyclic Graphs

# Acyclic Graphs

# Dense Graph

# Sparse Graph

# Completely Connected Graph

# Graph Weights
# Weighted vs Unweighted
# Can be used to represent anything that will affect the routing algorithm (like distance, hills etc.)

# Representing Graphs:

# Adjacency List
# Adjacency Matrices/Matrixes

# class LinkedListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class GraphNode:
#     def __init__(self, value):
#         self.value = value
#         self.weight = None


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        """Add edge from v1 to v2."""
        # If both are in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph.")

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return ("Vertex does not exist in graph.")

    def bft(self, starting_vertex_id):
        q = Queue()
        q.enqueue(starting_vertex_id)

        visited = set()

        while q.size() > 0:

            v = q.dequeue()

            if v not in visited:
                print(v)

                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


g1 = Graph()
g1.add_vertex(99)
g1.add_vertex(3)
g1.add_vertex(3490)
g1.add_edge(99, 3490)
g1.add_edge(99, 3)  # Connected node 99 to node 3
g1.add_edge(3, 99)  # Connected node 3 to node 99
# print(g1.get_neighbors(3))
g1.bft(99)
