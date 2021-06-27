from dataclasses import dataclass


@dataclass
class Scoop:
    flavor: str


@dataclass
class Bowl:
    scoops = []
    max_scoops = 3

    def add_scoops(self, *args):
        for scooper in args:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(scooper)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)
