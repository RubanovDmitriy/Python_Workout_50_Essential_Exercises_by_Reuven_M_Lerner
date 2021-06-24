class Scoop():
    def __init__(self, flavor: str) -> None:
        self.flavor = flavor


def create_scoops() -> None:
    scoops = [Scoop('chocolate'),
              Scoop('vanilla'),
              Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)
