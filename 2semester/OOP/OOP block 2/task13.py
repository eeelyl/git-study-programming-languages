class Individual:
    Counter = 0

    def __init__(self, character_name):
        self.character_name = character_name
        self.happy = True
        Individual.Counter += 1
        self.id = Individual.Counter

    def get_character_name(self):
        return self.character_name

    def is_happy(self):
        return self.happy

    def switch_mood(self):
        self.happy = not self.happy

    def speak(self):
        if self.happy:
            return f"Привет, я {self.character_name}"
        else:
            return "Уходи!"

    def __str__(self):
        return f"individual: [{self.id} {self.character_name}]"

    def __repr__(self):
        return f"individual: [{self.id} {self.character_name}]"


class Droid(Individual):
    def __init__(self, character_name):
        super().__init__(character_name)
        self.species = "droid"

    def speak(self):
        return "Beep Beep Beep"


class Biological(Individual):
    def __init__(self, character_name, height, mass, homeworld, species):
        super().__init__(character_name)
        self.height = height
        self.mass = mass
        self.homeworld = homeworld
        self.species = species

    def get_height(self):
        return self.height

    def get_mass(self):
        return self.mass

    def get_homeworld(self):
        return self.homeworld

    def get_species(self):
        return self.species

    def get_bmi(self):
        return self.mass / (self.height * self.height)


class Population:
    def __init__(self):
        self.population = []

    def add_individual(self, individual):
        self.population.append(individual)

    def get_highest_bmi_individual(self):
        biological_individuals = [
            individual for individual in self.population if isinstance(individual, Biological)]
        if not biological_individuals:
            return None
        return max(biological_individuals, key=lambda x: x.get_bmi())


population = Population()

population.add_individual(Droid("R2-D2"))
population.add_individual(Biological(
    "Luke Skywalker", 1.72, 77, "Tatooine", "human"))
population.add_individual(Biological(
    "Leia Organa", 1.5, 50, "Alderaan", "human"))
population.add_individual(Droid("C-3PO"))

highest_bmi_individual = population.get_highest_bmi_individual()
if highest_bmi_individual:
    print("Индивид с наибольшим индексом массы тела:", highest_bmi_individual)
