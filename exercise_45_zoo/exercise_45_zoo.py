from dataclasses import dataclass


@dataclass
class Zoo():
    cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)

    def __repr__(self):
        return '\n'.join(str(cage) for cage in self.cages)

    def animals_by_color(self, color):
        return [
            animal for cage in self.cages
            for animal in cage.animals
            if animal.color == color
        ]

    def animals_by_legs(self, number_of_legs):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs == number_of_legs]

    def number_of_legs(self):
        return sum(
            one_animal.number_of_legs
            for one_cage in self.cages
            for one_animal in one_cage.animals
        )
