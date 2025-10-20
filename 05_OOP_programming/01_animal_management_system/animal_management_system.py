class Animal:

    zoo_name = "Jadi's zoo"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def __str__(self):
        return f"{self.name}, {self.species}, {self.age}, {self.sound}"

    def info(self):
        print(f"Zoo: {Animal.zoo_name}\n")
        print("Animal:")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Sound: {self.sound}")

    def make_sound(self):
        return f"{self.name} is {self.sound}ing"


class Bird(Animal):

    def __init__(self, name, species, age, sound, wind_span):
        Animal.__init__(self, name, species, age, sound)
        self.wind_span = wind_span

    def make_sound(self):
        return f"{self.name} is chirp like {self.sound}"
    def __str__(self):
        return f"""Name: {self.name}
Age: {self.age}
Species: {self.species}
Sound: {self.sound}
Wind span: {self.wind_span}"""
    


animal = Animal("Lion", "African", 8, "grrrruaaaalllll")

print(animal.make_sound())

print()

animal.info()

print()

print(animal)

print()

bird = Bird("Pigeion", "Mourning Doves", 1, "Moosa Koo Taghi", 12)

print(bird)