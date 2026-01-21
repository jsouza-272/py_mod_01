#!python3
"""Garden security system module with validation.

This module implements a SecurePlant class with private attributes and
validation methods to ensure only valid data is accepted.
"""


class SecurePlant:
    """Represents a plant with secure, validated attributes.

    This class uses private attributes (name-mangled with __) and provides
    getter/setter methods with validation to prevent invalid data.

    Attributes:
        __name (str): The private name of the plant.
        __height (int): The private height of the plant in centimeters.
        __age (int): The private age of the plant in days.
    """

    def __init__(self, name, height, age):
        """Initialize a new SecurePlant instance with validation.

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
            age (int): The initial age of the plant in days.
        """
        self.__name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        """Get the plant's current height.

        Returns:
            int: The height of the plant in centimeters.
        """
        return self.__height

    def set_height(self, new_height):
        """Set the plant's height with validation.

        Args:
            new_height (int): The new height in centimeters.
            Must be non-negative.
        """
        if new_height < 0:
            t_aux = "Invalid operation attempted:"
            print(f"{t_aux} height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    def get_age(self):
        """Get the plant's current age.

        Returns:
            int: The age of the plant in days.
        """
        return self.__age

    def set_age(self, new_age):
        """Set the plant's age with validation.

        Args:
            new_age (int): The new age in days. Must be non-negative.
        """
        if new_age < 0:
            t_aux = "Invalid operation attempted:"
            print(f"{t_aux} age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {new_age} days [OK]")

    def get_info(self):
        """Get formatted information about the plant.

        Returns:
            str: A string containing the plant's name, height, and age.
        """
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print()
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant.get_info()}")
