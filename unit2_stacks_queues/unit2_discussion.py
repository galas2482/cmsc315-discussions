"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._stack = []
        # self._stack represents the array/list data structure as the foundation for the stack
       

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # when "pushing" or appending a new item/value to the stack, it allows for
        # the most recently pushed item to be "popped" or removed from the stack
        # allowing for LIFO
        self._stack.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        if self.is_empty(): raise RuntimeError("Cannot pop from an empty stack!");
        # if the stack is empty raise error since there are no values to pop from
      
        return self._stack.pop()
        #return the top of the arr/stack using the pop method which removes and returns the last item from a stack

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty(): raise RuntimeError("Cannot peek from an empty stack!")
        # peeking gets and returns the top/most recent value in the array without
        # deleting it
        # thus we return the last item using convinient python negative indexing here as -1 represents the last item
        return self._stack[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self._stack) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._queue = deque()
        # a deque is from what I understand a double ended queue, which allows for 
        # faster queue operations than a normal python list


    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self._queue.append(value)
        # the enqueue operation stores the most recentely added value at rear
        # of the queue, which then allows for them to be dequeued at the front 
        # and this preserves FIFO since the oldest items are removed and returned first
        # . We do this via append in python since it will add at the end

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty(): raise RuntimeError("Cannot dequeue from an empty queue since there is nothing to dequeue!")
        # an empty queue has nothing to dequeue, meaning an error is appropriate to throw since it is empty at this point
        return self._queue.popleft()
        # remove and return the oldest  item

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty(): raise RuntimeError("Queue is empty, there are no items to view")
        # front returns the oldest  item
        return self._queue[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self._queue) == 0
        


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\n=== STACK DEMO ===")
    print("Downloading all of your purchased games...")
    game_stack = Stack()
    game_1 = "Last of Us Part I"
    game_2 = "Final Fantasy VII Rebirth"
    game_3 = "Minecraft"
    game_4 = "The Legend of Zelda: Breath of the Wild"
    print(f"Downloading: {game_1}")
    game_stack.push(game_1)
    print(f"Downloading: {game_2}")
    game_stack.push(game_2)
    print(f"Downloading: {game_3}")
    game_stack.push(game_3)
    print(f"Downloading: {game_4}")
    game_stack.push(game_4)

    print("After you finish each game they will be removed (popped) from your Game Stack")
    print(f"{game_stack.pop()} finished! Removing now...")
    print(f"{game_stack.pop()} finished! Removing now...")
    print(f"{game_stack.pop()} finished! Removing now...")
    print(f"{game_stack.pop()} finished! Removing now...")

    # lets say user tries to delete a game that hasnt been downloaded
    # use try except to handle errors and allow program to keep running
    try:
        game_stack.pop() # will throw an error since there are no items
    except RuntimeError as error:
        print("Oh no! It seems as though you tried to delete a game that hasn't been downloaded")

    try:
        game_stack.peek() # will throw an error since there are no items
    except RuntimeError as error:
        print("There are no games to preview (peek) since there are no games purchased (no items)")

    one_stack = Stack()
    print(f"Creating a stack with the ring to rule all of the 7 Realms...")
    one_stack.push("The One Ring")
    one_stack.pop()
    if one_stack.is_empty(): print("The One Ring has been destroyed.")

    

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    restaurant_queue = Queue()
    print("Welcome to the Enzo's Italian Restaurant!")
    order_1 = "Spaghetti Carbonara"
    order_2 = "Pasta alla Norma"
    order_3 = "Margherita Pizza"
    order_4 = "Gnocchi"
    print(f"Taking (enqueue) Order 1: {order_1}!")
    restaurant_queue.enqueue(order_1)
    print(f"Taking (enqueue) Order 2: {order_2}!")
    restaurant_queue.enqueue(order_2)
    print(f"Taking (enqueue) Order 3: {order_3}!")
    restaurant_queue.enqueue(order_3)
    print(f"Taking (enqueue) Order 4: {order_4}!")
    restaurant_queue.enqueue(order_4)

    print(f"Finished cooking (dequeue) Order 1: {order_1}")
    restaurant_queue.dequeue()
    print(f"Finished cooking (dequeue) Order 2: {order_2}")
    restaurant_queue.dequeue()
    print(f"Finished cooking (dequeue) Order 3: {order_3}")
    restaurant_queue.dequeue()
    print(f"Finished cooking (dequeue) Order 4: {order_4}")
    restaurant_queue.dequeue()

    try:
        restaurant_queue.dequeue() # will throw an error because there are no items to dequeue
    except RuntimeError as error:
        print("It seems as though the kitchen was trying to cook with no orders in...")

    try:
        restaurant_queue.front()
    except RuntimeError as error:
        print("It seems like the kitchen was trying to see what order was next when there were no orders")

    goat_queue = Queue()
    print("The GOAT of Football is entering the league")
    goat_queue.enqueue("Tom Brady")
    goat_queue.dequeue()
    if goat_queue.is_empty(): print("The GOAT has retired...")


    

if __name__ == "__main__":
    main()
