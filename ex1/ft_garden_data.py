#!python3
"""Garden plant data management module.

This module defines a Plant class to store plant information and demonstrates
creating and displaying a collection of plants in a garden registry.
"""


class Plant:
    """Represents a plant with basic attributes.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        age (int): The age of the plant in days.
    """

    def __init__(self, name, height, age):
        """Initialize a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plants = [Plant("Rose", 25, 30),
              Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120)]
    print("=== Garden Plant Registry ===")
    for p in plants:
        print(f"{p.name}: {p.height}cm, {p.age} days old")
