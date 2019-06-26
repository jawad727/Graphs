

class Queue():
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
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors: # For every pair in ancestors we will add each value as individual nodes into our graph
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # (build edges in reverse)
        graph.add_edge(pair[1], pair[0])

    # (track the longest path length and the earliest ancestor node)
    # max = 1 because every path is at least 1 long - earliest = -1 because thats what we return when none of the nodes match our target
    max_path_len = 1
    earliest_ancestor = -1

    # Do a BFS from starting_node to each other node
    q = Queue() # - list of lists with paths in them
    q.enqueue([starting_node]) # - add a path with the starting node to list

    while q.size() > 0:
        path = q.dequeue() # - Path = latest path in the queue (commander Q)
        current_room = path[-1] # - Current_room = the last room we were in 

        # if the length of our current path == the max path variable AND our current room is smaller (or comes first alphabetically) do the following..
        # OR if the length of our current path is greater than the max path variable we will do the following..
        if (len(path) == max_path_len and current_room < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = current_room # setting a new earliest ancestor 
            max_path_len = len(path) # setting a new max path length

        for neighbor in graph.vertices[current_room]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    # Return the earliest ancestor
    return earliest_ancestor




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))
print('asd')