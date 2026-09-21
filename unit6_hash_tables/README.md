# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

This assignment encouraged me to dive deep into topics such as key-value access, hashing, hashing collisions, open addressing, and the algorithmic complexity of Hash Table. One challenge I encountered was actually how to model one of the edge cases, specifically the missing key access in an empty dictionary. So I actually used the .get method at first to use the empty dictionary key access, thinking it would provide an error to display, but I completely forgot that .get returns None if no matching key is found, which would have prevented me from displaying what I actually wanted to display. I worked through this by simply changing it to bracket based access. The Hash Table ADT is built around key-value pairs. To optimize efficiency for retrieving values using keys (e.g., getting account information using a user id), the data structure puts a key through an efficient hashing algorithm, getting a correspondent index for the underlying array, and then finally storing/accessing/deleting the desired value from that array in O(1) time vs O(n) time for a linear data structure. Collisions happen when two different keys map to the same index. A working hash table always handles collisions. CPython handles this with open addressing where if one value is already stored at an index, it probes/looks for another available index. 