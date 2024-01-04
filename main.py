def main():
    menu = int(input('Выберите пункт меню: 1. Вход, 2. Регистрация, 3. Выход'))
    if menu == 1:
       log()
    if menu == 2:
       reg()
    if menu == '3':
        exit()


def reg():
    login = input('логин: ')
    password = input(' пароль')
    with open('67', 'r') as file:
        for i in file.readlines():
            user = i.split(':')
            if login == user[0]:
                print('имя занято')
        if len(login) >= 3 and len(login) <= 20:
                print('Логин от 3 до 20 символов')
                reg()
        if len(password) >= 4 and len(password) <= 32:
                print('пароль от 3 до 20 символов')
                reg()
    with open('67', 'a') as file:
            file.write(f'{login}:{password}\n')

def log():
    login = input('логин: ')
    with open('67', 'r') as file:
        for i in file.readlines():
            user = i.split(':')
            if login == user[0]:
                password = input(' пароль')
                if password == user[1]:
                    print(f' Привет {login}')
                    exit()

if __name__ == '__main__':
    main()