"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class VideoGameCharacter:
    MAX_LEVEL = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"The name of this video game character is {self.name}, and they are {self.age} years old. The max level of a character in this video game is {VideoGameCharacter.MAX_LEVEL}")



# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SwordsMan(VideoGameCharacter):
    WEAPON_TYPE = "Sword"

    def __init__(self, name, age, sword_name, stamina, inventory=None):
        super().__init__(name, age)
        self.sword_name = sword_name
        self.stamina = stamina
        self.inventory = inventory if inventory is not None else []

    def attack(self):
        print(f"{self.name} attacks with their {self.sword_name}!")

    def display_info(self):
        print(f"{self.name} is a swordsman with a weapon of type {SwordsMan.WEAPON_TYPE}, and they are {self.age} years old with {self.stamina} stamina and inventory {self.inventory}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    swordsman1 = SwordsMan("Cloud Strife", 21, "Buster Sword", 100)
    swordsman2 = SwordsMan("King Arthur", 25, "Excalibur", 75)

    print(f"Class variable via class (SwordsMan.WEAPON_TYPE): {SwordsMan.WEAPON_TYPE}")
    print(f"Class variable via instance (swordsman1.WEAPON_TYPE): {swordsman1.WEAPON_TYPE}")

    swordsman1.shield = "Iron Shield"
    print(f"\nAdded 'shield' attribute to swordsman1: {swordsman1.shield}")

    print(f"\nswordsman1 instance namespace (__dict__): {swordsman1.__dict__}")
    print(f"swordsman2 instance namespace (__dict__): {swordsman2.__dict__}")

    print(f"\nSwordsMan class namespace (__dict__): {SwordsMan.__dict__}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = SwordsMan("sephiroth", 90, "Masamune", 100, inventory=["Health Potion", "Map"])

    shallow_hero = copy(original)

    deep_hero = deepcopy(original)

    """
    The difference between a shallow and deep copy is that, while a shallow copy creates a new object in memory,
    it still keeps references to the original data source; meaning that if one were to modify the objects via the 
    shallow copy, they would persist to the original copy as well. However, one can still add/modify the new data
    structure/object itself with no issue. A deep copy creates a new object AND creates new objects in memory for 
    every original object that there was. Meaning that changes to the new deep copy will not affect the original
    object created.
    """

    print("Before modifying original inventory:")
    print(f"Original Inventory:     {original.inventory}")
    print(f"Shallow Copy Inventory: {shallow_hero.inventory}")
    print(f"Deep Copy Inventory:    {deep_hero.inventory}")

    original.inventory.append("Elixir")

    print("\nAfter adding 'Elixir' to Original Inventory:")
    print(f"Original Inventory:     {original.inventory}")
    print(f"Shallow Copy Inventory: {shallow_hero.inventory}")
    print(f"Deep Copy Inventory:    {deep_hero.inventory} ")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    npc = VideoGameCharacter("Villager", 35)
    npc.display_info()

    hero = SwordsMan("Link", 17, "Master Sword", 90, inventory=["Shield", "Bombs"])
    hero.display_info()
    hero.attack()

    demonstrate_namespaces()
    demonstrate_copying()

if __name__ == "__main__":
    main()