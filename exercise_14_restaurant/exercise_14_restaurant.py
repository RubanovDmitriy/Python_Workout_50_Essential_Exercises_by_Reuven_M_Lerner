MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}


def restaurant():
    total = 0
    while True:
        order = input('Order: ').strip()
        if not order:
            break
        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} costs {price}, total is {total}')
        else:
            print(f'{order} isn’t in stock')

    print(f'Your total is {total}')


if __name__ == '__main__':
    restaurant()
