class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs, and sounds like {self.sound}'


class WolfS(Animal):
    sound = 'AUF'

    def __init__(self, color):
        super().__init__(color, 4)


class SheepS(Animal):
    sound = 'BE'

    def __init__(self, color):
        super().__init__(color, 4)


class SnakeS(Animal):
    sound = 'PST'

    def __init__(self, color):
        super().__init__(color, 0)


class ParrotS(Animal):
    sound = 'KRYA'

    def __init__(self, color):
        super().__init__(color, 2)
