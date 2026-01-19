#!python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.old_height = height
        self.height = height
        self.p_age = age

    def get_info(self):
        t_aux = f"{self.name} ({self.__class__.__name__}):"
        return f"{t_aux} {self.height}cm, {self.p_age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def unic(self):
        self.bloom()

    def get_info(self):
        return super().get_info() + f" {self.color} color"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = 3.14 * (self.trunk_diameter ** 2) / 100
        print(f"{self.name} provides {shade:.0f} square meters of shade")

    def unic(self):
        self.produce_shade()

    def get_info(self):
        return super().get_info() + f" {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name, height, age,  harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutri_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def unic(self):
        self.get_nutri_value()

    def get_info(self):
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
