import pytest

from exercise_43_animals.exercise_43_animal_sound import WolfS, SheepS, SnakeS, ParrotS
from exercise_43_animals.exercise_43_animals import Wolf, Sheep, Snake, Parrot
from exercise_43_animals.exercise_43_leged_animals import WolfL, SheepL, SnakeL, ParrotL


@pytest.mark.parametrize(('species', 'color', 'output'), [
    (Wolf, 'black', 'black Wolf, 4 legs'),
    (Sheep, 'white', 'white Sheep, 4 legs'),
    (Snake, 'brown', 'brown Snake, 0 legs'),
    (Parrot, 'green', 'green Parrot, 2 legs')
])
def test_animal(species, color, output):
    a = species(color)
    assert str(a) == output


@pytest.mark.parametrize(('species', 'color', 'output'), [
    (WolfL, 'black', 'black WolfL, 4 legs'),
    (SheepL, 'white', 'white SheepL, 4 legs'),
    (SnakeL, 'brown', 'brown SnakeL, 0 legs'),
    (ParrotL, 'green', 'green ParrotL, 2 legs')
])
def test_legged_animal(species, color, output):
    a = species(color)
    assert str(a) == output


@pytest.mark.parametrize(('species', 'color', 'output'), [
    (WolfS, 'black', 'black WolfS, 4 legs, and sounds like AUF'),
    (SheepS, 'white', 'white SheepS, 4 legs, and sounds like BE'),
    (SnakeS, 'brown', 'brown SnakeS, 0 legs, and sounds like PST'),
    (ParrotS, 'green', 'green ParrotS, 2 legs, and sounds like KRYA')
])
def test_animal_sound(species, color, output):
    a = species(color)
    assert str(a) == output
