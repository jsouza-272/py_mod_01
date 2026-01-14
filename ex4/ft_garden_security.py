#!python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.lower().capitalize()
        print(f"Plant created: {self.name}")
        self.__height = None
        self.__age = None
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self.__height

    def set_height(self, height: int) -> None:
        if height < 0:
            print()
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return
        self.__height = height
        print(f"Height updated: {height}cm [OK]")

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
            return
        self.__age = age
        print(f"Age updated: {age} days [OK]")

    def info(self) -> str:
        return f"{self.name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    plant = SecurePlant("rose", 20, 30)
    print(f"Current plant: {plant.info()}")
