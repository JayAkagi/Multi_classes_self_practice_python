from .animal import Animal
class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise Exception("Only add Instance of Animal")
        self.animals.append(animal)

    def all_sound(self):
        for animal in self.animals:
            print(f"{animal.name}: {animal.sound}!")