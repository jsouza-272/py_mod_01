#!python3
"""Garden analytics and management system module.

This module implements a comprehensive garden management system with multiple
classes demonstrating inheritance, static/class methods, inner classes, and
various OOP patterns for tracking plants, gardens, and analytics.
"""


class Plant:
    """Base plant class with growth tracking.

    Attributes:
        name (str): The name of the plant.
        height (int): The current height of the plant in centimeters.
        st_height (int): The starting height of the plant.
        age (int): The age of the plant in days.
    """

    def __init__(self, name, height, age):
        """Initialize a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The initial height in centimeters.
            age (int): The initial age in days.
        """
        self.name = name
        self.st_height = height
        self.height = height
        self.age = age

    def grow(self):
        """Grow the plant by 1 centimeter and print a message."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def growth(self):
        """Calculate total growth from starting height.

        Returns:
            int: The difference between current and starting height.
        """
        return self.height - self.st_height

    def get_info(self):
        """Get formatted information about the plant.

        Returns:
            str: The plant's name and height.
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A plant that can produce flowers and bloom.

    Attributes:
        color (str): The color of the flower.
    """

    def __init__(self, name, height, age, color):
        """Initialize a new FloweringPlant instance.

        Args:
            name (str): The name of the plant.
            height (int): The initial height in centimeters.
            age (int): The initial age in days.
            color (str): The color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def blooming(self):
        """Check if the plant is blooming based on height.

        Returns:
            bool: True if height is greater than 20, False otherwise.
        """
        if self.height > 20:
            return True
        return False

    def get_info(self):
        """Get formatted information about the flowering plant.

        Returns:
            str: Plant info with color and blooming status.
        """
        if self.blooming():
            return super().get_info() + f", {self.color} flower (blooming)"
        return super().get_info() + f", {self.color} flower (not blooming)"


class PrizeFlower(FloweringPlant):
    """A flowering plant that has prize points.

    Attributes:
        prize (int): The number of prize points awarded to this flower.
    """

    def __init__(self, name, height, age, color, prize):
        """Initialize a new PrizeFlower instance.

        Args:
            name (str): The name of the flower.
            height (int): The initial height in centimeters.
            age (int): The initial age in days.
            color (str): The color of the flower.
            prize (int): The prize points value.
        """
        super().__init__(name, height, age, color)
        self.prize = prize

    def get_info(self):
        """Get formatted information about the prize flower.

        Returns:
            str: Plant info with prize points.
        """
        return super().get_info() + f", Prize point: {self.prize}"


class Garden:
    """Represents a garden containing multiple plants.

    WARNING: This class uses a mutable default argument (plants: list = [])
    in __init__, which can lead to unexpected
    behavior if not handled carefully.
    The same default list instance is shared across all Garden instances that
    don't provide their own plants list. This is intentional for demonstration
    purposes but is generally considered an anti-pattern in Python.

    Attributes:
        g_name (str): The name of the garden.
        plant_st (int): The starting number of plants.
        plant_add (int): The number of plants added.
        plants (list): List of Plant objects in the garden.
        score (int): The calculated score based on prize flowers.
    """

    def __init__(self, g_name, plants: list = [], plant_qnt=0):
        """Initialize a new Garden instance.

        Args:
            g_name (str): The name of the garden.
            plants (list, optional): Initial list of plants. Defaults to [].
                WARNING: Uses mutable default argument - the same list instance
                is shared across Garden instances that don't provide plants.
            plant_qnt (int, optional): Initial plant quantity. Defaults to 0.
        """
        self.g_name = g_name
        self.plant_st = plant_qnt
        self.plant_add = plant_qnt
        self.plants = plants
        self.score = self.calc_score()

    def add_plant(self, plant):
        """Add a plant to the garden and update the score.

        Args:
            plant (Plant): The plant to add to the garden.
        """
        self.plants.append(plant)
        self.plant_add += 1
        self.score = self.calc_score()
        print(f"Added {plant.name} to {self.g_name}'s garden")

    def p_in_g(self):
        """Print all plants currently in the garden."""
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p.get_info()}")

    def total_growth(self):
        """Calculate total growth of all plants in the garden.

        Returns:
            int: Sum of growth for all plants.
        """
        growth = 0
        for p in self.plants:
            growth += p.height - p.st_height
        return growth

    def calc_score(self):
        """Calculate the garden score based on prize flowers.

        Returns:
            int: Total prize points from all PrizeFlower instances.
        """
        score = 0
        for p in self.plants:
            if type(p) is PrizeFlower:
                score += p.prize
        return score

    def growth_all(self):
        """Grow all plants in the garden."""
        for p in self.plants:
            p.grow()


class GardenManager:
    """Manages multiple gardens with static and class methods.

    Attributes:
        gardens (list): List of Garden objects being managed.
        total_gardens (int): Count of total gardens managed.
    """

    def __init__(self):
        """Initialize a new GardenManager instance."""
        self.gardens = []
        self.total_gardens = self.count_gardens(self.gardens)

    @classmethod
    def create_garden_network(cls, garden: Garden):
        """Create a garden network with the given garden and Bob's garden.

        Args:
            garden (Garden): A garden to add to the network.

        Returns:
            GardenManager: A manager instance with multiple gardens.
        """
        g_manager = cls()
        bobs_plants = [Plant("Oak Tree", 100, 365),
                       FloweringPlant("Rose", 25, 30, "red"),
                       PrizeFlower("Sunflower", 50, 30, "yellow", 5)]
        bobs = Garden("Bob", bobs_plants, 3)
        g_manager.add_garden(garden)
        g_manager.add_garden(bobs)
        return g_manager

    def add_garden(self, garden: Garden):
        """Add a garden to the manager.

        Args:
            garden (Garden): The garden to add.
        """
        self.gardens.append(garden)
        self.total_gardens += 1

    @staticmethod
    def count_gardens(gardens: list):
        """Count the number of gardens in a list.

        Args:
            gardens (list): List of gardens to count.

        Returns:
            int: The number of gardens.
        """
        count = 0
        for g in gardens:
            count += 1
        return count

    class GardenStats:
        """Inner class for analyzing garden statistics.

        Attributes:
            garden (Garden): The garden being analyzed.
            g_manager (GardenManager): The manager containing the garden.
        """

        def __init__(self, garden, g_manager):
            """Initialize a new GardenStats instance.

            Args:
                garden (str): Name of the garden to analyze.
                g_manager (GardenManager): The garden manager.
            """
            self.garden = self.set_garden(garden, g_manager)
            self.g_manager = g_manager

        def set_garden(self, garden, g_manager):
            """Find and set the garden by name.

            Args:
                garden (str): The name of the garden to find.
                g_manager (GardenManager): The manager to search in.

            Returns:
                Garden or None: The found garden, or None if not found.
            """
            for g in g_manager.gardens:
                if g.g_name == garden:
                    return g
            print("Error: Garden not found")
            return None

        @staticmethod
        def plant_status(garden: Garden):
            """Display plant status for a garden.

            Args:
                garden (Garden): The garden to analyze.
            """
            txt1 = f"Plants added: {garden.total_growth()}"
            txt2 = f"Total growth: {garden.total_growth()}cm"
            print(f"{txt1}, {txt2}")

        @staticmethod
        def types(garden: Garden):
            """Display plant type distribution in a garden.

            Args:
                garden (Garden): The garden to analyze.
            """
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
            """Check if all plants in all gardens have valid heights.

            Returns:
                bool: True if all heights are non-negative, False otherwise.
            """
            for g in self.g_manager.gardens:
                for p in g.plants:
                    if p.height < 0:
                        return False
            return True

        def scores(self):
            """Get formatted scores for all gardens.

            Returns:
                str: Comma-separated garden scores.
            """
            txt = ""
            count = 0
            for g in self.g_manager.gardens:
                txt += f"{g.g_name}: {g.score}"
                count += 1
                if count < self.g_manager.total_gardens:
                    txt += ", "
            return txt

        def status(self):
            """Display comprehensive status report for the garden."""
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
