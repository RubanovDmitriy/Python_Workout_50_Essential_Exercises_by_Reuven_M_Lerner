def get_rainfall():
    result = {}

    while True:
        city = input('City: ').strip()
        if not city:
            break
        rainfall = int(input('Rainfall: '))
        result[city] = result.get(city, 0) + int(rainfall)

    for city, rain in result.items():
        print(f'{city}: {rain}')


if __name__ == '__main__':
    get_rainfall()
