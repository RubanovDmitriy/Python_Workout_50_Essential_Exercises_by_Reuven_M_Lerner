class Scoop():
    def __init__(self, flavor: str) -> None:
        self.flavor = flavor


class Bowl():
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for scooper in args:
            self.scoops.append(scooper)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)
