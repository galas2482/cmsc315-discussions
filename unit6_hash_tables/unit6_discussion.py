"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    print("\n=== INSERT OPERATIONS ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # a dictionary is a data structure that emulates a hash table by holding key value pairs to store data for
    # fast O(1) average lookups (although collision can cause this to degrade in some cases). A key is hashed using a hashing algorithm and is given an index in which that hash
    # maps to. The value tied to that key is then stored in that array slot, allowing for O(1) lookups.
    # What happens if two keys share the same hashed index? CPython under the hood basically 
    # does this thing called "open addressing" where it probes for another slot index
    user_id_and_names = {}
    user_id_and_names[1001] = "Luca"
    user_id_and_names[1002] = "John"
    user_id_and_names[1003] = "Isaiah"
    user_id_and_names[1004] = "Mateo"
    user_id_and_names[1005] = "David"
    
    # id and user name dictionary/hash table to model key/value pairing
 
    # use Python's helpful for key/value loop structure to loop through all key value pairs in the dict
    for key, value in user_id_and_names.items():
        print(f"The user id: {key} belongs to a person named: {value}.")

    print(user_id_and_names) # print like normal too

    print("\n=== LOOKUP OPERATIONS ===")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.
    
    # As mentioned above, when key-accessed retrieval/lookup is used, 
    # the key is hashed using an efficient hashing algorithm that gives
    # a corresponding index in the underlying array/list, and then the
    # value at that index is retrieved
    name_one = user_id_and_names.get(1001)
    # use first key
    print(f"The first name retrieved from the dictionary is: {name_one}") # print value retrieved from first key
    name_two = user_id_and_names.get(1002)
    # use second key
    print(f"The second name retrieved from the dictionary is: {name_two}") # print value retrieved from the second key

    print("\n=== UPDATE OPERATIONS ===")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    # again the key is hashed to get the index, but this time instead of just accessing the array value
    # at the hashed index, it is updated with the new value, leading to O(1) updates. No duplicate keys are created
    # so the dictionary size stays the same 
    before_value = user_id_and_names.get(1003) # get before val
    print(f"Name and dict before update - Name: {before_value}, Dictionary: {user_id_and_names}") # print before 
    user_id_and_names[1003] = "Benjamin" # update value for existing key
    after_value = user_id_and_names.get(1003) # get after val
    print(f"Name after update - Name: {after_value}, Dictionary: {user_id_and_names}") # print after

    print("\n=== DELETE OPERATIONS ===")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    # When a key is removed, the key and the value are removed from the dictionary;
    # the key is used to get the hashed index and then that is used to delete the value
    # from the underlying array. CPython under the hood marks the slot as a placeholder and
    # so probing for other collisions still works.
    print(f"Dictionary of user ids and names before deletion of 4th key {user_id_and_names}.") # print dict before
    del user_id_and_names[1004] # delete key val pair
    print(f"Dictionary of user ids and names after deletion of 4th key {user_id_and_names}.") # print dict after

    print("\n=== EDGE CASES ===")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    # create empty dictionary
    empty_dict = {}

    # A try except is necessary here as accessing a key from an empty dict, which thus 
    # doesn't exist, will raise a KeyError (for any missing key). Under the hood, no key is found,
    # the call fails, and hence you have a KeyError.
    try:
        empty_dict["Cool key"] # fake key name 
    except KeyError as error:
        print(f"Cannot access a nonexistent key. Raised error {error}") # message printed when error is run into

    # using pop with the default parameter returns that default in case of an empty key instead of a KeyError
    # and leaves the dictionary unchanged
    result = user_id_and_names.pop("Non-existent key", None) # use pop with fake key and None to safely check/delete and prevent
    print(f"Safe delete of missing key returned: {result}.") # erroneous behavior if key doesnt exist



if __name__ == "__main__":
    main()