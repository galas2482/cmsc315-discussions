"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value # initialize value first
        self.left = None # then set left to null/None
        self.right = None # then right


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self._root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        if value is None: raise RuntimeError("Cannot insert a null value in a BST") # edge case handling - makes no sense to insert a null val
        self._root = self._insert_recursive(self._root, value) # call recursivel with root as starting node

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None: return Node(value) # base case - position found, create new node then return for assingment purposes

        if value < node.value: # value is less than current node, and thus we recurse left
            node.left = self._insert_recursive(node.left, value) 
        elif value > node.value: # value is greater than current node, so we recurse right
            node.right = self._insert_recursive(node.right, value)
        else: # edge case - value == node.value, print a messsage saying duplicates are not allowed
            print("Cannot insert duplicate values in this BST!")
            return node # self assignment 


        return node # self assignment for if and elif statements

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        if value is None: raise RuntimeError("Cannot search for a value of null") # handle edge case of null value
        return self._search_recursive(self._root, value) # call recusrive search

        # because of it's binary logic, a BST search each iteration eliminates half of its search space, or
        # time that it would spend searching that area, leading to an average/best case of O(log n), which again,
        # halves the search time every iteration as opposed to linear's O(n)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None: return False # value was not found anwhere in tree

        if value < node.value: # value is less, so recurse left
            return self._search_recursive(node.left, value)
        elif value > node.value: # value is greater so recurse right
            return self._search_recursive(node.right, value)
        else: # value == node.value aka value is found! Return True
            return True

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = [] # initialize values
        self._inorder_recursive(self._root, values) # call recursive traversal method
        return values # return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None: return # reached end of tree
        self._inorder_recursive(node.left, values) # visit left subtree
        values.append(node.value) # visit current node and 
        self._inorder_recursive(node.right, values) # visit right subtree 

        # since a nodes left value in a bst will always be less than the nodes value,
        # and a nodes right value is greater, the order of left -> node -> right allows for
        # the values to be traversed in ascending order which will always produce a sorted array
        # of values


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    # create BST then insert ages at each subtree

    print("\n=== TREE CONSTRUCTION ===")

    family_ages = BST()
    uncle_rico_age = 42
    family_ages.insert(uncle_rico_age)
    print(f"Age of Uncle Rico: {uncle_rico_age}")
    aunt_maria_age = 34
    family_ages.insert(aunt_maria_age)
    print(f"Age of Aunt Maria: {aunt_maria_age}")
    cousin_vinny_age = 47
    family_ages.insert(cousin_vinny_age)
    print(f"Age of Cousin Vinny: {cousin_vinny_age}")
    grandpa_george_age = 70
    family_ages.insert(grandpa_george_age)
    print(f"Age of Grandpa George: {grandpa_george_age}")
    nephew_luca_age = 25
    family_ages.insert(nephew_luca_age)
    print(f"Age of Nephew Luca: {nephew_luca_age}")
    cousin_michael_age = 64
    family_ages.insert(cousin_michael_age)
    print(f"Age of Cousin Michael: {cousin_michael_age}")
    sister_sarah_age = 38
    family_ages.insert(sister_sarah_age)
    print(f"Age of Sister Sarah: {sister_sarah_age}")

    # a BST is efficient since the search space to insert/search for a value is reduced by half at each step
    # meaning that the correct place for insertion is able to found much, much easier


    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    ages_in_order = family_ages.inorder()
    print(ages_in_order)
    # this traversal  will produce a sorted output since in a BST a strict ruling
    # of the left node being less than the current, and the right being greater than,
    # leads you via in_order traversal to traversing the left first then the current, then
    # the right

    print("\n=== SEARCH TESTS ===")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    ages = [42, 25, 100, 19] # two of these do exist, two fo them don't in this tree

    for age in ages:
        if family_ages.search(age): # if age is in tree print a message saying it is 
            print(f"Someone has the age of {age} in the family tree!")
        elif not family_ages.search(age): # if age isnt in tree print a message saying it isn't
            print(f"Nobody has the age of {age} in the family tree...")


    print("\n=== EDGE CASES ===")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    try: # try except since searching for None/null throws an error
        family_ages.search(None)
    except RuntimeError as error: # catch error
        print("Nobody in this tree could have an age of null/None")



if __name__ == "__main__":
    main()