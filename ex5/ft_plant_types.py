#!python3


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.lower().capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> None:
        type = self.__class__.__name__
        print(self)
        print(self.__class__)
        print(self.__class__.__name__)
        return f"\n{self.name} ({type}): {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return super().get_info() + f", {self.color} color"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = (3.14 * (self.trunk_diameter ** 2)) / 100
        print(f"Oak provides {shade:.0f} square meters of shade")

    def get_info(self) -> str:
        return super().get_info() + f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value.capitalize()

    def nutri_value(self) -> None:
        print(f"{self.name} is rich in viatamin {self.nutritional_value}")

    def get_info(self) -> str:
        return super().get_info() + f", {self.harvest_season} harvest"


if __name__ == "__main__":
    rose = Flower("Rose", 5, 10, "red")
    sunflower = Flower("sunflower", 20, 40, "yellow")
    oak = Tree("oak", 500, 1825, 50)
    birch = Tree("birch", 700, 2000, 40)
    tomato = Vegetable("tomato", 80, 90, "summer", "C")
    potato = Vegetable("potato", 5, 80, "summer", "c")
    print("=== Garden Plant Types ===")
    print(rose.get_info())
    rose.bloom()
    print(sunflower.get_info())
    sunflower.bloom()
    print(oak.get_info())
    oak.produce_shade()
    print(birch.get_info())
    birch.produce_shade()
    print(tomato.get_info())
    tomato.nutri_value()
    print(potato.get_info())
    potato.nutri_value()
