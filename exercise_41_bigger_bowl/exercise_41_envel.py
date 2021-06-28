from dataclasses import dataclass


class NotEnoughPostageError(Exception):
    pass


@dataclass
class Envelope:
    postage_multiplier = 10
    weight: float
    postage: int
    was_sent: bool

    def add_postage(self, amount):
        self.postage += amount

    def send(self):
        if self.postage >= self.weight * self.postage_multiplier:
            self.was_sent = True
        else:
            raise NotEnoughPostageError('Not enough postage')


class BigEnvelope(Envelope):
    postage_multiplier = 15
