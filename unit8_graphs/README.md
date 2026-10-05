# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

So, this assignment helped me understand how BFS works instead of just memorizing it. A queue's First-In, First-Out (FIFO) order is what makes BFS explore level by level, analogous to ripples in a pond, and a visited list prevents revisiting nodes and infinite loops. I also practiced building adjacency lists and tracing traversal order by hand. My main challenges were small bugs and designing the graph. I first called bfs without passing the graph, which caused a TypeError. Tracing my edges also helped show me that my graph was directed and partly disconnected, so some vertices were unreachable from my start vertex. I fixed this by tracing the levels manually and adding a guard so empty graphs or invalid start vertices return an empty list instead of crashing. BFS works by using a queue and visits all neighbors before going deeper, so it finds fewest-edge paths in unweighted graphs. DFS utilizes a stack or recursion and follows one path as deep/far down as possible before backtracking. BFS fits shortest paths in unweighted graphs (Dijkstra's algorithm extends this idea to weighted ones), social network degrees of separation, and network broadcasting. DFS fits cycle detection, maze solving, and topological sorting.
