#!python3

class Plant:
    def __init__(self, name: str, st_height, st_age):
        self.name = name.lower().title()
        self._st_heigth = st_height
        self._st_age = st_age
        self._heigth = st_height
        self._age = st_age

    def info(self) -> str:
        return f"- {self.name}: {self._heigth}cm"

    def grow(self):
        self._heigth += 1
        print(f"{self.name} grew 1cm")

    def age(self):
        self._age += 1

    def update(self):
        self.age()
        self.grow()


class FloweringPlant(Plant):
    def __init__(self, name, st_height, st_age, flower_color: str):
        super().__init__(name, st_height, st_age)
        self.flower_color = flower_color.lower()
        self.bloom_status = self.bloom()

    def info(self) -> str:
        return super().info() + f", {self.flower_color} flowers " + \
            f"({self.bloom_status})"

    def bloom(self):
        if self._age > 5:
            return "blooming"
        return "not blooming"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, st_height, st_age, flower_color, prize_points):
        super().__init__(name, st_height, st_age, flower_color)
        self.prize_points = prize_points

    def info(self) -> str:
        return super().info() + f", Prize points: {self.prize_points}"


class Garden:
    def __init__(self, owner: str, plants: list = []):
        self.owner = owner.lower().capitalize()
        self.g_name = self.owner + "'s"
        self.plants = plants
        self.score = 0
        self.set_score()

    def add_plant(self, plant) -> None:
        self.plants.append(plant)
        m = f"Added {plant.name} {plant.__class__.__name__}"
        self.set_score()
        print(f"{m} to {self.g_name} garden")

    def grow_all_plants(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.update()

    def set_score(self):
        for p in self.plants:
            if type(p) is PrizeFlower:
                self.score += p.prize_points

    def get_score(self) -> str:
        return f"{self.owner}: {self.score}"


class GardenManager:
    def __init__(self):
        self.gardens = []

    @classmethod
    def create_garden_network(cls):
        manager = cls()
        garden1 = Garden("alice")
        plant2 = [Plant("oak tree", 100, 365),
                  FloweringPlant("rose", 5, 10, "red"),
                  PrizeFlower("violet", 6, 15, "purple", 5)]
        garden2 = Garden("bob", plant2)
        manager.add_garden(garden1)
        manager.add_garden(garden2)

        return manager

    def add_garden(self, garden: Garden):
        self.gardens.append(garden)

    def grow_plants(self, garden: str):
        garden = garden.lower().capitalize()
        for g in self.gardens:
            if g.owner == garden:
                g.grow_all_plants()

    class GardenStatus:
        def __init__(self, garden_manager):
            self.g_manager = garden_manager

        def status(self, garden: str):
            nbr_g = 0
            for g in self.g_manager.gardens:
                if g.owner == garden.lower().capitalize():
                    print(f"\n=== {g.g_name} Garden Report ===")
                    for plant in g.plants:
                        print(plant.info())
                    total = f", Total growth: {self.calc_grow(g)}cm"
                    print(f"\nPlants added: {self.calc_add(g)}{total}")
                    p_types = self.check_types(g)
                    t = f"Plant types: {p_types['r']} regular, "
                    t2 = f"{p_types['f']} flowering, "
                    print(f"{t}{t2}{p_types['p']} prize flowers")
                flag1 = self.height_validation(g)
                flag2 = self.height_validation(g)
                nbr_g += 1
            if flag1 != flag2:
                flag1 = False
            print(f"\nHeight validation test: {flag1}")
            print(f"Garden scores - {self.get_score()}")
            print(f"Total gardens managed: {nbr_g}")

        def get_score(self):
            s = ""
            v = 0
            for i in self.g_manager.gardens:
                v += 1
            current = 0
            for g in self.g_manager.gardens:
                s += g.get_score()
                if current < v - 1:
                    s += ", "
                current += 1
            return s

        @staticmethod
        def calc_grow(garden: Garden):
            total_grow = 0
            for p in garden.plants:
                total_grow += p._heigth - p._st_heigth
            return total_grow

        @staticmethod
        def height_validation(garden: Garden):
            for p in garden.plants:
                if p._heigth <= 0:
                    return False
            return True

        @staticmethod
        def check_types(garden: Garden):
            p_types = {
                'r': 0,
                'f': 0,
                'p': 0
            }
            for p in garden.plants:
                if type(p) is Plant:
                    p_types['r'] += 1
                elif type(p) is FloweringPlant:
                    p_types['f'] += 1
                elif type(p) is PrizeFlower:
                    p_types['p'] += 1
            return p_types

        @staticmethod
        def calc_add(garden: Garden):
            i = 0
            for p in garden.plants:
                i += 1
            return i


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    plant1 = [Plant("oak tree", 100, 365),
              FloweringPlant("rose", 25, 10, "red"),
              PrizeFlower("tulip", 50, 15, "white", 10)]
    g_manager = GardenManager.create_garden_network()
    for g in g_manager.gardens:
        if g.owner == "Alice":
            for p in plant1:
                g.add_plant(p)
    g_status = GardenManager.GardenStatus(g_manager)
    g_manager.grow_plants("alice")
    g_status.status("alice")
