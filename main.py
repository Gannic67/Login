def get_menu() -> None:
    menu = int(input('Выберите пункт меню: 1. Вход, 2. Регистрация, 3. Выход'))
    if menu == 1:
        get_login()
    if menu == 2:
        get_registration()
    if menu == '3':
        exit()


def get_registration() -> None:
    try:
        login = int(input('логин: '))
        password = int(input(' пароль'))
        with open('Baza', 'r') as file:
            for i in file.read().split('\n'):
                user = i.split(':')
        if login == user[0]:
            print('имя занято')
        if login in range(3, 15):
            print('Логин должен быть от 3 до 15 символов')
            get_registration()
        if password in range(3, 20):
            print('пароль должен быть от 3 до 20 символов')
            get_registration()
        with open('Baza', 'a') as file:
            file.write(f'{login}:{password}\n')
    except ValueError:
        print('Вы ввели буквы, а надо цифры')
    except FileNotFoundError:
        with open('Base', 'a', encoding='utf-8'):
            pass
        get_login()


def get_login() -> None:
    try:
        login = input('логин: ')
        with open('Baza', 'r') as file:
            for i in file.read().split('\n'):
                user = i.split(':')
                if login == user[0]:
                    password = input('пароль: ')
                    if password == user[1]:
                        print(f' Привет {user[0]}')
                        exit()

    except ValueError:
        print('Вы ввели буквы, а надо цифры')

def check_file():
    try:
        with open('Baza', 'r') as file:
            print('Файл найден')
    except FileNotFoundError:
        print('Файл не найден')


if __name__ == '__main__':
    get_menu()