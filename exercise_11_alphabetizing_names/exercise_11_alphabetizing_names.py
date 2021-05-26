import operator

PEOPLE = [
    {
        'first': 'Reuven',
        'last': 'Lerner',
        'email': 'reuven@lerner.co.il'
     },
    {
        'first': 'Donald',
        'last': 'Trump',
        'email': 'president@whitehouse.gov'
    },
    {
        'first': 'Vladimir',
        'last': 'Putin',
        'email': 'president@kremvax.ru'
    }
]


def alphabetize_names(people):
    return sorted(people, key=operator.itemgetter('last', 'first'))
