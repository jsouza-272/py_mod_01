#!python3

class SecurePlant:
    def __init__(self, name, height, age):
        self.__name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        if new_height < 0:
            t_aux = "Invalid operation attempted:"
            print(f"{t_aux} height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age < 0:
            t_aux = "Invalid operation attempted:"
            print(f"{t_aux} age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {new_age} days [OK]")

    def get_info(self):
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print()
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant.get_info()}")
