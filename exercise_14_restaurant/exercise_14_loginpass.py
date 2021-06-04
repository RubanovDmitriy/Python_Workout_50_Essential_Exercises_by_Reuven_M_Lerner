CREDS = {
    'Dalanonys@gmail.com': 'gBLFZKYzVR',
    'Kairlassi@gmail.com': '01AFyVKBYX',
    'Xineva@gmail.com': 'XZJGo0niwL',
    'Nevin@gmail.com': '0sX1mYwkQF',
    'Cordenatr@gmail.com': '1NQb11GbAB',
    'Lexilli@gmail.com': 'fj2Fh7pHOD',
    'Xavonata@gmail.com': 'xZEZmVjgAz',
    'Hanevivel@gmail.com': 'F6StMbyFnM',
    'Xenollen@gmail.com': 'h6iTOD1XnL',
    'Llintashi@gmail.com': '79Xm2VAnK6',
}


def login_pass():
    login = input('Login: ').strip()
    passwd = input('Password: ').strip()
    if login in CREDS:
        if passwd == CREDS[login]:
            print('You successfully authorized')
        else:
            print('Your password is incorrect')
    else:
        print('No such login in DataBase')


if __name__ == '__main__':
    login_pass()
