#!python3
"""Plant factory module with creation tracking.

This module demonstrates plant creation with automatic logging and tracking
of how many plants are created in the factory pattern.
"""

class Plant:
    """Represents a plant with growth tracking and creation logging.
    
    Attributes:
        name (str): The name of the plant.
        height (int): The current height of the plant in centimeters.
        old_height (int): The height of the plant before the current week.
        p_age (int): The age of the plant in days.
    """

    def __init__(self, name, height, age):
        """Initialize a new Plant instance and log its creation.
        
        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
            age (int): The initial age of the plant in days.
        """
        self.name = name
        self.old_height = height
        self.height = height
        self.p_age = age
        print(f"Created: {self.name} ({self.height}cm, {self.p_age} days)")

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
    print("=== Plant Factory Output ===")
    plants = [Plant("Rose", 25, 30),
              Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90),
              Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120),]
    len = 0
    for p in plants:
        len += 1
    print(f"\nTotal plants created: {len}")
