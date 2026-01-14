#!python3

class Plant:
    def __init__(self, name: str, st_height, st_age):
        self.name = name.lower().capitalize()
        self.st_heigth = st_height
        self.st_age = st_age
        self.heigth = st_height
        self.age = st_age

    def get_info(self) -> str:
        return f"{self.name}: {self.heigth}cm, {self.age} days"


class FloweringPlant(Plant):
    def __init__(self, name, st_height, st_age, flower_color: str):
        super().__init__(name, st_height, st_age)
        self.flower_color = flower_color.lower()
        self.bloom_status = self.bloom()

    def get_info(self) -> str:
        return super().get_info() + f", {self.flower_color} flowers " + \
            f"({self.bloom_status})"

    def bloom(self):
        if self.age > 5:
            return "blooming"
        return "not blooming"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, st_height, st_age, flower_color, prize_points):
        super().__init__(name, st_height, st_age, flower_color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        return super().get_info() + f", Prize points: {self.prize_points}"


class Garden:
    def __init__(self, owner: str, plants: list):
        self.owner = owner.lower().capitalize()
        self.garden_name = self.owner + "'s"
        self.plants = plants

# class GardenManager:


if __name__ == "__main__":
    plants = [Plant("oak", 100, 365), FloweringPlant("rose", 5, 10, "red"),
              PrizeFlower("tulip", 6, 15, "white", 5)]
    garden = Garden("alice", plants)
    for plant in garden.plants:
        print(plant.get_info())
    print(garden.garden_name)
