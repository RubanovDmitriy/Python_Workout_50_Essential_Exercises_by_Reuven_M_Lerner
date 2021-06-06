import statistics


def get_rainfall():
    result = {}

    while True:
        city = input('City: ').strip()
        if not city:
            break
        rainfall = int(input('Rainfall: '))

        if city not in result:
            result[city] = []
        result[city].append(int(rainfall))
        print(result.get(city))

    for city, rain in result.items():
        print(f'{city} Total: {rain}, Average: {round(statistics.mean(rain), 2)}')


if __name__ == '__main__':
    get_rainfall()
