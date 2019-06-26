"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add[v2]
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex): # Checks first floor first with all rooms then second etc
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue() # List of all rooms we need to go to starts off blank
        q.enqueue(starting_vertex) # Adds room to list that we will search
        visited = set() # List of rooms we have visited, it starts off blank

        while q.size() > 0: # While list Q a value we will searcch
            current_vert = q.dequeue() # Cross off the newest room in list and look in it ; current_vert = current room
            if current_vert not in visited: # If this room we are looking at isnt in list SET do the following
                print(current_vert) # Print room to add to continuously building path
                visited.add(current_vert) # Add to visited so we wont go back there


                for neighbor_vert in self.vertices[current_vert]: # {room1 : [room2, room3, room4]}
                    q.enqueue(neighbor_vert) 
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        s = Stack() # List of all rooms we need to go to starts off blank
        s.push(starting_vertex) # Adds starting floor
        visited = set() # List of room we have visited, starts off blank

        while s.size() > 0: # While there is at lease one room we need to explore do the following

            v = s.pop() # Crosses off one room and looks in it ; v = current room

            if v not in visited: # If we havent looked in the current room do this

                print(v) # Print that we looked in it
                visited.add(v) # Add current room into visited rooms list

                for next_vert in self.vertices[v]: # For every next_room we see in verticies[current_room] add it to the list of all rooms we need to search
                    s.push(next_vert)



    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass  # TODO

        
        def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue() # Commander he has the list of all the possible paths we can take
        q.enqueue([starting_vertex]) # Adding starting room to the path
        visited = set() # Commander Set has a empty list

        while q.size() > 0: # While commander Q has more than 0 rooms to search
            path = q.dequeue() # Path = [403] path equals the path created earlier
            current_room = path[-1] # Current room is just last value in the PATH array

            if current_room not in visited: # If commander Set does not have this room in his list do the following
                if current_room == destination_vertex: # if room were in right now equals the destination return the path we took to get here
                    return path
                visited.add(current_room) # tell commander Set to add room to visited rooms

                for room_same_floor in self.vertices[current_room]:

                    copy_path = list(path) # copy_path = [...5th_floor_rooms, 401, 402] ; current_room = 403
                    copy_path.append(room_same_floor) # adding neighboring rooms
                    q.enqueue(copy_path)
        return None





    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
