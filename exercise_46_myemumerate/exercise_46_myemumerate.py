from dataclasses import dataclass


@dataclass
class MyEnumerate():
    data: str
    index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        value = (self.index, self.data[self.index])
        self.index += 1
        return value
