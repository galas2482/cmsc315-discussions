# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

Reflection:

Over this assignment, I learned about the List Abstract Data Type (ADT), and how to implement a list and its core operations (insert, delete, search) using a Python list. One challenge I encountered was how to determine what an edge case was for the deletion operation. After cross referencing real world scenarios, I realized by tracing what would cause a real IndexError in Python, that there were 3 invalid cases: an index greater than the length of the list, trying to access an index from an empty list, and trying to access an element less than 0. This normally triggers an index out of bounds error. The performance of the list implementations are crucial as they are not only extensively used themselves, but also in other data structures. Imagine a scenario where movie indices are cached, and you need to present the searched movie. An array in this case will provide O(1) performance for an indexed-based retrieval whereas a linked list will slow down to provide an O(n) performance even with an index. Due to this, as programmers, we need to take into account the performance of the different implementations of the List ADT.