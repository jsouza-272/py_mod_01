#!python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.old_height = height
        self.height = height
        self.p_age = age

    def grow(self):
        self.height += 1

    def age(self):
        self.p_age += 1

    def grow_age(self):
        self.grow()
        self.age()

    def pass_week(self):
        self.old_height = self.height
        for i in range(6):
            self.grow_age()

    def get_info(self):
        t_aux = f"{self.name}: {self.height}cm, {self.p_age} days old"
        if self.height - self.old_height > 0:
            t_aux2 = f"Growth this week: +{self.height - self.old_height}cm"
            return f"{t_aux}\n{t_aux2}"
        return f"{t_aux}"


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(plant.get_info())
    plant.pass_week()
    print("=== Day 7 ===")
    print(plant.get_info())
