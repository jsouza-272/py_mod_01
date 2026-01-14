#!python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.heigth = height
        self.days_old = age
        self.start_heigth = height

    def grow(self) -> None:
        self.heigth += 1

    def age(self) -> None:
        self.days_old += 1

    def pass_a_week(self) -> None:
        i = 0
        while i < 6:
            self.grow()
            self.age()
            i += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.heigth}cm, {self.days_old} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 30, 45)
    cactus = Plant("Cactus", 15, 120)
    i = 0
    print("=== Day 1 ===")
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()
    rose.pass_a_week()
    sunflower.pass_a_week()
    cactus.pass_a_week()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.heigth - rose.start_heigth}cm")
    sunflower.get_info()
    print(f"Growth this week: +{sunflower.heigth - sunflower.start_heigth}cm")
    cactus.get_info()
    print(f"Growth this week: +{cactus.heigth - cactus.start_heigth}cm")
