"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # worst case is that target is at the end, and thus you would have to check
    # every element of the n elements one at a time giving O(n) complexity
    for index, item in enumerate(lst): # use enumerate to iterate over index and item using a more efficient for each loop
        if item == target: return index # if value at current value equals target, return that index

    return -1 # target wasn't found


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    lo = 0
    hi = len(lst)-1 # set hi and lo to beginning and end of list (length)

    # each iteration, half of the remaining search space is removed,
    # so after k comparisons say, you narrow it down to n / 2^k elements,
    # which is why it only takes about log2(n) steps instead of n, giving 
    # O(log n) complexity
    while lo <= hi: # condition that tells us if we have exhausted our search space
        mid = lo + (hi-lo) // 2 # get mid
        if lst[mid] == target: # if found return index of mid
            return mid
        elif lst[mid] < target: # if current val is less than target, switch to right
            lo = mid+1
        else:
            hi = mid-1 # if current val is greater than target, switch to left

    return -1 # target wasn't found


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    # using sorted to ensure binary search works correctly
    movies = sorted(["Inception", "Whiplash", "Good Will Hunting", "Star Wars: The Empire Strikes Back",
                     "Dune 2", "Before Sunrise", "Pulp Fiction"])

    print("\n=== SMALL DATASET TEST ===")
    print("List of movies: ", movies) # print out list for reference

    # value that exists
    target = "Good Will Hunting"
    print(f"\nLooking for {target}")
    print("Linear Search: ", linear_search(movies, target))
    print("Binary Search: ", binary_search(movies, target))

    # value that doesn't exist
    new_target = "Titanic"
    print(f"\nSearching for {new_target}")
    print("Linear Search: ", linear_search(movies, new_target))
    print("Binary Search: ", binary_search(movies, new_target))
    # both return -1 but binary search gets there way faster since it eliminates
    # half of the remaining search space in each step

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    import time

    # range gives us sorted numbers from 0 to 1 million
    big_nums = list(range(0, 1000000, 2))

    print("\n=== LARGE DATASET TEST ===")
    print(f"List size: {len(big_nums)} elements") # show list size 

    num_target = 750000 # target (about 3/4 through list)

    start = time.perf_counter()
    linear_result = linear_search(big_nums, num_target) # linear search result
    end = time.perf_counter()
    linear_time = end - start
    
    start = time.perf_counter()
    binary_result = binary_search(big_nums, num_target) # binary search result
    end = time.perf_counter()
    binary_time = end - start

    print(f"Time for Linear Search: {linear_time:.6f}")
    print(f"Time for Binary Search: {binary_time:.6f}")
    # difference between O(n) search time vs O(log n) search time



    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # empty list edge case
    empty_lst = []
    print("Empty list edge case: ")
    print("Linear Search: ", linear_search(empty_lst, 100))
    print("Binary Search: ", binary_search(empty_lst, 100))
    # since both return -1 if the target item isn't found, the functions
    # will both immediately terminate, and thus return -1

    #single value/element list
    single_val = [11]
    print("Single element list edge case: ")
    print("Linear Search: ", linear_search(single_val, 11))
    print("Binary Search: ", binary_search(single_val, 11))


if __name__ == "__main__":
    main()