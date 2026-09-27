"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    sort_lst = list(lst) # copy the list

    for i in range(len(sort_lst)): # outer loop the controls current iteration of comparison loop
        # each iteration of the comparison loop
        swapped = False # boolean for optimization
        for j in range(len(sort_lst)-i-1): # comparison loop: this is where all the magic happens and where
            # the values are compared against each other
            if sort_lst[j] > sort_lst[j+1]: # if value at j > j+1, then swap and this will help elements "bubble up"
                sort_lst[j], sort_lst[j+1] = sort_lst[j+1], sort_lst[j]
                swapped = True

        if not swapped:
            break # if no elements were swapped in the first comparison passthrough, it is already sorted

    return sort_lst # return sorted list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    if len(lst) <= 1: return lst # base case where an empty list or of length 1 is already sorted

    mid = len(lst) // 2 # get mid as half the length of list

    left_half = merge_sort(lst[:mid]) #recurse on left half
    right_half = merge_sort(lst[mid:]) # recurse on right half

    return merge(left_half, right_half) # call merge helper function to merge both left and right
    # then return     


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    merged_lst = [] # merged array
    i = 0 # pointer for left side
    j = 0 # pointer for right side 

    while i < len(left) and j < len(right): # compare elements from both sides to append to results
    # sort of like a two pointer method
        if left[i] <= right[j]: # if the current value being evaluated
            # in the left array is smaller than the right, append it.
            merged_lst.append(left[i])
            i += 1
        else:
            # now, if the current value being evaluated in the 
            # right array is smaller than the left, append it.
            merged_lst.append(right[j])
            j += 1

    # once the loop finishes, append the rest of the items that might be
    # remaining in either half
    merged_lst.extend(left[i:]) 
    merged_lst.extend(right[j:])

    return merged_lst # return the result



def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    movie_ratings = [9.3, 8.4, 8.2, 7.7, 7.1, 7.9, 8.0, 8.2, 7.4] # unsorted list of floats of movie ratings out of 10
    print(f"Here is our imported list of movie ratings from users: {movie_ratings}.") # print original list

    bubble_result = bubble_sort(movie_ratings) # sort using bubble sort
    merge_result = merge_sort(movie_ratings) # sort using merge sort

    print(f"Here is the updated, sorted list after using the bubble sort algorithm: {bubble_result}.") # print bubble sort result
    print(f"Here is the updated, sorted list after using the merge sort algorithm: {merge_result}.") # print merge sort result    

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    galaga_leaderboard = [2100, 1450, 850, 735, 9000, 2555, 2000] # build a leaderboard of galaga scores
    print(f"Here is our imported list of Galaga scores from users: {galaga_leaderboard}.") # print original list

    bubble_result = bubble_sort(galaga_leaderboard) # sort using bubble sort
    merge_result = merge_sort(galaga_leaderboard) # sort using merge sort

    print(f"Here is the updated, sorted list after using the bubble sort algorithm: {bubble_result}.") # print bubble sort result
    print(f"Here is the updated, sorted list after using the merge sort algorithm: {merge_result}.") # print merge sort result    

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # nothing changes in this first edge case because the base case in merge sort is triggered, and in bubble sort the loop terminates instantly,
    # meaning that it returns the empty list it was provided.
    empty_lst = []
    print(f"Here is the empty list before sorting: {empty_lst}") # print empty before (not gonna change)

    bubble_empty = bubble_sort(empty_lst) # sort using bubble sort (this won't change anything)
    merge_empty = merge_sort(empty_lst) # sort using merge sort (this won't change anything either)

    print(f"Here is the empty list after bubble sort: {bubble_empty}. As you can notice, nothing changed.") # show that nothing changes using bubble
    print(f"Here is the empty list after merge sort: {merge_empty}. As you can notice, nothing changed.") # show that nothing changes using merge


    # nothing changes in this second edge case because, again, the base case in merge sort is triggered, and in bubble sort the loop terminates almost instantly,
    # meaning that it returns the single-element list it was provided.
    one_lst = [5]
    print(f"Here is the single-element list before sorting: {one_lst}") # print empty before (not gonna change)

    bubble_one = bubble_sort(one_lst) # sort using bubble sort (this won't change anything)
    merge_one = merge_sort(one_lst) # sort using merge sort (this won't change anything either)

    print(f"Here is the single-element list after bubble sort: {bubble_one}. As you can notice, nothing changed.") # show that nothing changes using bubble
    print(f"Here is the single-element list after merge sort: {merge_one}. As you can notice, nothing changed.") # show that nothing changes using merge    


if __name__ == "__main__":
    main()