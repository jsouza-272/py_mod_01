#!python3
'''
This program creates 3 plants with different names, heights, and ages,
and displays their information on the screen.
'''


class Plant:
    '''
    Represents a plant.

    Attributes:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters (cm).
        age (int): Age of the plant in days.
    '''
    def __init__(self, name: str, height: int, age: int) -> None:
        '''
        Initializes a Plant instance.

        :param name: Name of the plant.
        :type name: str
        :param height: Height of the plant in centimeters (cm).
        :type height: int
        :param age: Age of the plant in days.
        :type age: int
        '''
        self.name = name.capitalize()
        self.heigth = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 30, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.heigth}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.heigth}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.heigth}cm, {cactus.age} days old")
