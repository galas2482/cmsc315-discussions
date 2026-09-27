# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

Through this assignment, I gained concrete sorting skills by implementing two fundamental sorting algorithms: merge sort and bubble sort. While implementing these algorithms, I also learned their algorithmic complexities (O(n^2) for bubble and O(n log n) for merge), their respective iterative and recursive approaches, and how they handled a variety of edge cases. The biggest challenge I encountered was the recursive dividing logic and its helper function. I overcame this challenge by just picking a very simple example, an array of 8 elements, and going through the algorithm on paper. This paper exercise enabled me to understand the workflow, but also to divide and conquer responsibilities for the main function and the helper function. After this, I returned to the laptop and laid out what I had, iteratively refining the code until it matched the necessary logic that I had prepared to test it against in the main() function. Another challenge/learning opportunity I encountered was optimization for the bubble sort algorithm. I overcame this by implementing a boolean swapped that keeps track of whether or not the first comparison loop made a full runthrough without swapping any values; if it didn't, it would end the loop early, optimizing performance. From what I understand, merge sort is better than bubble sort in almost every case. Especially as the size of the dataset increases, merge sort runs in O(n log n) average time complexity while bubble sort runs in O(n^2), making a huge difference in time for large datasets. However, if you have a rather small dataset, and you need a quick and easy solution to sort, and you don't have access to any built-in sorting algorithms, bubble sort can prove to be useful in certain situations.