#!python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.old_height = height
        self.height = height
        self.p_age = age
        print(f"Created: {self.name} ({self.height}cm, {self.p_age} days)")

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
    print("=== Plant Factory Output ===")
    plants = [Plant("Rose", 25, 30),
              Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90),
              Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120),]
    len = 0
    for p in plants:
        len += 1
    print(f"\nTotal plants created: {len}")
