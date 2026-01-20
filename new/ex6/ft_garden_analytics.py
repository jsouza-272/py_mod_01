#!python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.st_height = height
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def growth(self):
        return self.height - self.st_height

    def get_info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def blooming(self):
        if self.height > 20:
            return True
        return False

    def get_info(self):
        if self.blooming():
            return super().get_info() + f", {self.color} flower (blooming)"
        return super().get_info() + f", {self.color} flower (not blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize):
        super().__init__(name, height, age, color)
        self.prize = prize

    def get_info(self):
        return super().get_info() + f", Prize point: {self.prize}"


class Garden:
    def __init__(self, g_name, plants: list = [], plant_qnt=0):
        self.g_name = g_name
        self.plant_st = plant_qnt
        self.plant_add = plant_qnt
        self.plants = plants
        self.score = self.calc_score()

    def add_plant(self, plant):
        self.plants.append(plant)
        self.plant_add += 1
        self.score = self.calc_score()
        print(f"Added {plant.name} to {self.g_name}'s garden")

    def p_in_g(self):
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p.get_info()}")

    def total_growth(self):
        growth = 0
        for p in self.plants:
            growth += p.height - p.st_height
        return growth

    def calc_score(self):
        score = 0
        for p in self.plants:
            if type(p) is PrizeFlower:
                score += p.prize
        return score

    def growth_all(self):
        for p in self.plants:
            p.grow()


class GardenManager:
    def __init__(self):
        self.gardens = []
        self.total_gardens = self.count_gardens(self.gardens)

    @classmethod
    def create_garden_network(cls, garden: Garden):
        g_manager = cls()
        bobs_plants = [Plant("Oak Tree", 100, 365),
                       FloweringPlant("Rose", 25, 30, "red"),
                       PrizeFlower("Sunflower", 50, 30, "yellow", 5)]
        bobs = Garden("Bob", bobs_plants, 3)
        g_manager.add_garden(garden)
        g_manager.add_garden(bobs)
        return g_manager

    def add_garden(self, garden: Garden):
        self.gardens.append(garden)
        self.total_gardens += 1

    @staticmethod
    def count_gardens(gardens: list):
        count = 0
        for g in gardens:
            count += 1
        return count

    class GardenStats:
        def __init__(self, garden, g_manager):
            self.garden = self.set_garden(garden, g_manager)
            self.g_manager = g_manager

        def set_garden(self, garden, g_manager):
            for g in g_manager.gardens:
                if g.g_name == garden:
                    return g
            print("Error: Garden not found")
            return None

        @staticmethod
        def plant_status(garden: Garden):
            txt1 = f"Plants added: {garden.total_growth()}"
            txt2 = f"Total growth: {garden.total_growth()}cm"
            print(f"{txt1}, {txt2}")

        @staticmethod
        def types(garden: Garden):
            p_type = [0, 0, 0]
            for plant in garden.plants:
                if type(plant) is Plant:
                    p_type[0] += 1
                elif type(plant) is FloweringPlant:
                    p_type[1] += 1
                elif type(plant) is PrizeFlower:
                    p_type[2] += 1
            regular = f"{p_type[0]} regular"
            flowering = f"{p_type[1]} flowering"
            prize = f"{p_type[2]} prize flowers"
            print(f"Plant types: {regular}, {flowering}, {prize}")

        def height_valid(self):
            for g in self.g_manager.gardens:
                for p in g.plants:
                    if p.height < 0:
                        return False
            return True

        def scores(self):
            txt = ""
            count = 0
            for g in self.g_manager.gardens:
                txt += f"{g.g_name}: {g.score}"
                count += 1
                if count < self.g_manager.total_gardens:
                    txt += ", "
            return txt

        def status(self):
            self.garden.p_in_g()
            print()
            self.plant_status(self.garden)
            self.types(self.garden)
            print()
            print(f"Height validation test: {self.height_valid()}")
            print(f"Garden score - {self.scores()}")
            print(f"Total gardens managed: {self.g_manager.total_gardens}")


if __name__ == "__main__":
    alices_plants = [Plant("Oak Tree", 100, 365),
                     FloweringPlant("Rose", 25, 30, "red"),
                     PrizeFlower("Sunflower", 50, 40, "yellow", 10)]
    alice = Garden("Alice")
    print("=== Garden Management System Demo ===")
    print()
    for p in alices_plants:
        alice.add_plant(p)
    print("\nAlice is helping all plants grow...")
    alice.growth_all()
    manager = GardenManager.create_garden_network(alice)
    m_status = GardenManager.GardenStats("Alice", manager)
    print("\n=== Alice's Garden Report ===")
    m_status.status()
