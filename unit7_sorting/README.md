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

Through this assignment, I gained concrete sorting skills by implementing two fundamental sorting algorithms: merge sort and bubble sort. While implementing these algorithms, I learned their algorithmic complexities (O(n^2) for bubble and O(n log n) for merge), their respective iterative and recursive approaches, and how they handled edge cases. The biggest challenge I encountered was the recursive dividing logic and its helper function. I overcame this challenge by using an array, and going through the algorithm on paper. This helped me understand the workflow, and how responsibilities split between the main function and the helper function. After this, I then returned to the code and iteratively refined it until it matched that logic. Another challenge I encountered was optimizing the bubble sort algorithm. I addressed this with a swapped boolean that ends the loop early once a full pass makes no swaps. From what I understand, merge sort is better than bubble sort in almost every case. As the dataset size increases, merge sort's O(n log n) time complexity makes a huge difference over bubble sort's O(n^2). However, if you have a rather small dataset without access to built-in sorting algorithms, bubble sort can be useful in certain situations.