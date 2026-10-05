"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    if not graph or start < 0 or start >= len(graph):
        print("Either an empty graph was given as input or an invalid start index.")
        return []

    queue = deque() # create a queue, which introduces FIFO structure, that serves as the supporting data structure to create a "ripple effect"
    queue.append(start) # put in start to create starting point
    visited = [False] * len(graph) # create a visited list to track progress and reduce redundancy
    visited[start] = True
    search_list = [] # list to store vertices searched
    print("Commencing BFS Search...")

    while queue:
        current = queue.popleft() # track currently processed item
        neighbors = graph[current] # get a list of all vertices that the current vertex has adjacency to
        print(f"Current level/value in BFS Search {current}.") # print value at current vertex
        search_list.append(current) # add currently processed node to search_list


        for neighbor in neighbors: # loop through all the neighbors/adjacent vertices
            if not visited[neighbor]: # If the current vertex has not been visited, then add it to the queue to be processed.
                # Since a queue has a FIFO structure, this will cause the neighbors on the same "level" of the current vertex to be processed
                # before going "further down" the graph. This differs from Depth-First-Search (DFS), where a stack is implemented in lieu of 
                # a queue-resulting in a pattern where the deepest paths of one vertex are explored before moving horizontally. An oversimplified
                # way to look at it is just moving vertically instead of horizontally.
                visited[neighbor] = True
                queue.append(neighbor)

    return search_list


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")


    print("\n=== GRAPH STRUCTURE ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    graph = [[] for i in range(6)] # create adj list using list comprehension
    # each vertex is a person in a social media network and each edge is a one way follow
    graph[0].append(4) # the next 6 lines create adjacency between the vertices
    graph[0].append(2)
    graph[0].append(1)
    graph[1].append(2) # these are all edges 
    graph[2].append(1)
    graph[2].append(0)
    graph[3].append(5) 
    graph[4].append(0)
    graph[5].append(3)

    for vertex in range(len(graph)): # loop through all the vertices
        print(f"The vertex {vertex} has adjacency to following vertices {graph[vertex]}.")

    print("\n=== BFS TRAVERSAL ===")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    start_vertex = 1 # select starting node/vertex
    og_order = bfs(graph, start_vertex)
    print(f"BFS Traversal with original graph: {og_order}.")
    #  As i mentioned above, Since a BFS uses a queue, which has a FIFO structure, this will cause the neighbors on the same "level" of the current vertex to be processed
    # before going "further down" the graph. In layman's terms, it traverses horizontally rather than vertically. A great analogy can be drawn to dropping a rock in a pond:
    # as soon as you drop the rock it ripples
    graph[0].append(3)
    graph[1].append(4)
    new_order = bfs(graph, start_vertex)
    print(f"BFS Traversal with updated graph: {new_order}.")

    
    print("\n=== EDGE CASE TESTS ===")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    # edge case 1 you can an empty graph. The guard returns [] instead of crashing
    print("Empty graph: ", bfs([], 0))

    # edge case 2 is where you start from a vertex that doesn't exist as the graph only has 0-5.
    # Similarly, the [] will be returned and the statement will be printed.
    print("Invalid start: ", bfs(graph, 10))


if __name__ == "__main__":
    main()