class Animal():
    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class TwoLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 2


class FourLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 4


class ZeroLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 0


class WolfL(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class SheepL(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class SnakeL(ZeroLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class ParrotL(TwoLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)
