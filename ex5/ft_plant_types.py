#!python3
"""Plant type hierarchy module with inheritance.

This module demonstrates object-oriented inheritance with a base Plant class
and specialized subclasses for Flowers, Trees, and Vegetables, each with
unique behaviors and characteristics.
"""


class Plant:
    """Base class representing a generic plant.

    Attributes:
        name (str): The name of the plant.
        height (int): The current height of the plant in centimeters.
        old_height (int): The height of the plant before the current week.
        p_age (int): The age of the plant in days.
    """

    def __init__(self, name, height, age):
        """Initialize a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
            age (int): The initial age of the plant in days.
        """
        self.name = name
        self.old_height = height
        self.height = height
        self.p_age = age

    def get_info(self):
        """Get formatted information about the plant.

        Returns:
            str: A string containing the plant type, name, height, and age.
        """
        t_aux = f"{self.name} ({self.__class__.__name__}):"
        return f"{t_aux} {self.height}cm, {self.p_age} days"


class Flower(Plant):
    """Represents a flowering plant with color and blooming capability.

    Attributes:
        color (str): The color of the flower.
    """

    def __init__(self, name, height, age, color):
        """Initialize a new Flower instance.

        Args:
            name (str): The name of the flower.
            height (int): The initial height in centimeters.
            age (int): The initial age in days.
            color (str): The color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Display a message indicating the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")

    def unic(self):
        """Perform the flower's unique behavior (blooming)."""
        self.bloom()

    def get_info(self):
        return super().get_info() + f" {self.color} color"


class Tree(Plant):
    """Represents a tree with trunk diameter and shade production.

    Attributes:
        trunk_diameter (int): The diameter of the tree trunk in centimeters.
    """

    def __init__(self, name, height, age, trunk_diameter):
        """Initialize a new Tree instance.

        Args:
            name (str): The name of the tree.
            height (int): The initial height in centimeters.
            age (int): The initial age in days.
            trunk_diameter (int): The trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Calculate and display the shade coverage area of the tree."""
        shade = 3.14 * (self.trunk_diameter ** 2) / 100
        print(f"{self.name} provides {shade:.0f} square meters of shade")

    def unic(self):
        """Perform the tree's unique behavior (shade production)."""
        self.produce_shade()

    def get_info(self):
        """Get formatted information about the tree.

        Returns:
            str: Plant information including trunk diameter.
        """
        return super().get_info() + f" {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Represents a vegetable plant with harvest and nutritional information.

    Attributes:
        harvest_season (str): The season when the vegetable can be harvested.
        nutritional_value (str): The key nutritional value of the vegetable.
    """

    def __init__(self, name, height, age,  harvest_season, nutritional_value):
        """Initialize a new Vegetable instance.

        Args:
            name (str): The name of the vegetable.
            height (int): The initial height in centimeters.
            age (int): The initial age in days.
            harvest_season (str): The harvest season.
            nutritional_value (str): The nutritional value description.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutri_value(self):
        """Display the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def unic(self):
        """Perform the vegetable's unique behavior (display nutrition info)."""
        self.get_nutri_value()

    def get_info(self):
        """Get formatted information about the vegetable.

        Returns:
            str: Plant information including harvest season.
        """
        return super().get_info() + f" {self.harvest_season} harvest"


if __name__ == "__main__":
    plants = [Flower("Rose", 25, 30, "red"),
              Tree("Oak", 500, 1825, 50),
              Vegetable("Tomato", 80, 90, "summer", "vitamin C")]
    print("=== Garden Plant Types ===")
    print()
    for p in plants:
        print(p.get_info())
        p.unic()
        print()
