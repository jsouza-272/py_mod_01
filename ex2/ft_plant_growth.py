#!python3
"""Plant growth tracking module.

This module defines a Plant class with methods to track growth over time,
including weekly growth cycles and information retrieval.
"""


class Plant:
    """Represents a plant with growth tracking capabilities.

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

    def grow(self):
        """Increase the plant's height by 1 centimeter."""
        self.height += 1

    def age(self):
        """Increase the plant's age by 1 day."""
        self.p_age += 1

    def grow_age(self):
        """Perform both growth and aging in a single operation."""
        self.grow()
        self.age()

    def pass_week(self):
        """Simulate a week passing by growing and aging the plant 6 times."""
        self.old_height = self.height
        for i in range(6):
            self.grow_age()

    def get_info(self):
        """Get formatted information about the plant.

        Returns:
            str: A string containing the plant's name, height, and age,
                 with optional growth information if the plant has grown.
        """
        t_aux = f"{self.name}: {self.height}cm, {self.p_age} days old"
        if self.height - self.old_height > 0:
            t_aux2 = f"Growth this week: +{self.height - self.old_height}cm"
            return f"{t_aux}\n{t_aux2}"
        return f"{t_aux}"


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(plant.get_info())
    plant.pass_week()
    print("=== Day 7 ===")
    print(plant.get_info())
