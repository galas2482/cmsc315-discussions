# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

While completing this assignment, I developed a greater understanding of the practical difference between O(n) an O(log n) time complexity, not just as abstract notation but rather as something that I could actually measure and use in my future projects. Implementing binary search for me reinforced how narrowing the search space by half each iteration, instead of just checking every element, is what provides great efficiency, especially as the size of the data set grows

One challenge I ran into was a small but important bug regarding the comparisons: I initially wrote time.perf_counter without the parentheses when timing my searches, which returned the function object instead of the actual time and caused a type error that would've ruined my program. It was a good reminder to double check function calls against function references. I also had to be careful with binary search loop boundaries to avoid infinite loops or skipping the target. I almost put lo < hi instead of lo <= hi which would've prevented the search from successfully finding a one element list where lo = hi.

All in all, linear search is best for small or unsorted datasets where the overhead of sorting isn't worth it, while binary search is far more efficient for larger, sorted datasets, like searching through a list of IDs or records, where the O(log n) speedup becomes a significant differentiator as the dataset grows.