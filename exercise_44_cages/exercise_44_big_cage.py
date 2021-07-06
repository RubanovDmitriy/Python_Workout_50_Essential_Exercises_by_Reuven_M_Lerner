from dataclasses import dataclass


@dataclass
class BigCage():
    id_number: int
    animals = []
    max_animals = 5

    def add_animals(self, *animals):
        for animal in animals:
            if len(self.animals) < self.max_animals:
                self.animals.append(animal)

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal) for animal in self.animals)

        return output
