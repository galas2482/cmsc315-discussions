"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # After an item is inserted, existing elements are shifted to the right by one after the index
    # insertion. In a language like python, the memory is handled dynamically, so resizing is not an issue;
    # however, in languages like java or c++, c style arrays need extra handling to ensure the array has
    # enough contiguous memory to insert the new element and shift the appropriate elements.

    lst.insert(index, value) 

    # if an item is inserted at the beginning of the list
    # it can be a very timely operation because all the subsequent items would need to
    # be shifted in memory leading to worst case O(n) time. In contrast, insertion at 
    # the end of the list could be a constant O(1) assuming enough memory is allocated. 
    # This is why Linked-Lists are preferred in certain cases to allow for O(1) insertion at the beginning of a list.



def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Index validation is crucial for an indexed based function for any implementation
    # of the list ADT because whether the language is compiled or interpreted, or even a hybrid,
    # an invalid index will always cause an index-out-of-bounds error that abruptly stops the program.
    # Safe deletion, and returning None in the case of an invalid index, allows us to ensure no undefined
    # behavior takes place while ensuring the operation still functions seamlessly.

    if not lst or index < 0 or index >= len(lst): return None
    del_val = lst[index]
    del lst[index] # so removing at this index will shift every item to the left which can cause O(n) deletion in the worst case
    return del_val 



def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search since it scans over every single item in the list at least once.
    # Meaning that if there said to be n items in a list, this search will take O(n) time worst case,
    # and O(1) best case assuming the desired item is the first element.

    for index in range(len(lst)): 
        if lst[index] == value: return index
    return -1 # item wasn't found



def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # initial creation of list with some values (or in this case favorite movies)
    favorite_movies = ["Good Will Hunting", "Lord of the Rings: The Return of the King", "Terminator 2: Judgement Day"]
    
    # iterate through each movie, printing each movie
    for movie in favorite_movies:
        print(movie)

    # insert three favorite_movies, one at the beginning, one in the middle, and one at the end. 
    insert_at(favorite_movies, 0, "The Odyssey")
    print("Inserting at the beginning: ", favorite_movies) # print list after insert at the beginning
    insert_at(favorite_movies, (len(favorite_movies) // 2), "La La Land")
    print("Inserting at the middle: ", favorite_movies) # print list after insert at the middle
    insert_at(favorite_movies, (len(favorite_movies)), "Inception")
    print("Inserting at the end: ", favorite_movies) # print list after insert at the end

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    movie_one = delete_at(favorite_movies, 0) # delete and save value of deleted movie
    print(f"Watched movie from beginning of the list: {movie_one}. Movie list now: {favorite_movies}") # print deleted movie then the movie list after deleting the beginning movie
    movie_two = delete_at(favorite_movies, (len(favorite_movies) // 2)) # delete and save value of deleted movie
    print(f"Watched movie from the middle of the list: {movie_two}. Movie list now: {favorite_movies}") # print deleted movie then the movie list after deleting the middle movie of the list
    movie_three = delete_at(favorite_movies, (len(favorite_movies)-1)) # delete and save value of deleted movie
    print(f"Watched movie from the end of the list: {movie_three}. Movie list now: {favorite_movies}") # print deleted movie then the movie list after deleting the last movie in the list


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    real_movie_index = search_value(favorite_movies, "Good Will Hunting") # searches and retrieves of the index 
    # of the movie/value specified, which in this case does exist
    print(f"Searched for the movie 'Good Will Hunting'. Found at index: {real_movie_index}") # print the index the movie was found at
    non_existent_movie_index = search_value(favorite_movies, "The Godfather Part VIII") # not only is this movie not in the movie list.
    # This movie doesn't exist. Thus, by the logic of the function it will return 
    # the value -1 in order to signal that an invalid input has been given for this list
    print(f"Searched for the movie 'The Godfather Part VIII'. Not found and returned value: {non_existent_movie_index} signaling an erroneous search")
    # print the error code -1 to signal that an erroneous search was attempted

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    invalid_index = 10000000
    invalid_del = delete_at(favorite_movies, invalid_index) # there are obviously not 10000000 favorite_movies in the movie list, so this will trigger the edge case
    # in which the function will return None
    print(f"Tried to delete from index {invalid_index}, which is far greater than the length of the list: {len(favorite_movies)} and thus returned the value {invalid_del}. This value was returned in case of an invalid index.")
    # displays the invalid index, why it is invalid, and what it returned
    empty_lst = []
    empty_del = delete_at(empty_lst, 5)
    print(f"Tried to delete from the list empty list which as one can see, {empty_lst}, is empty. This triggered the edge case error-handling logic for the function and returned {empty_del}. This is because deleting from an empty list makes no sense as there is nothing to delete from.") 
    # displays the empty lst, why deleting from an empty list is erroneous behavior, and what it returned in this case.




if __name__ == "__main__":
    main()