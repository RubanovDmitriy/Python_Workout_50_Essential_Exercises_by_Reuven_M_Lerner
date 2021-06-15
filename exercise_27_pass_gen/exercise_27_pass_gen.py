import random


def create_password_generator(characters):
    def create_password(length):
        output = []
        for _ in range(length):
            output.append(random.choice(characters))
        return ''.join(output)

    return create_password
