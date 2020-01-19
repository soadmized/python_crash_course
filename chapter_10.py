import json

def get_stored_username():
    """
    Получает хранимое имя пользователя, если оно существует
    """
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """
    Запрашивает новое имя пользователя
    """
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """
    Приветствует пользователя по имени
    """
    username = get_stored_username()
    if username:
        while True:
            check_name = input("Is your name {}? y/n: ".format(username))
            if check_name == 'y':
                print("Welcome back, " + username + "!")
                break
            elif check_name == 'n':
                username = get_new_username()
                print("We'll remember you when you come back, " + username + "!")
                break
            else:
                print("Please enter y or n: ")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


if __name__ == "__main__":

    filename = 'Python Zen.txt'

    # файл целиком
    with open(filename) as file:
        t = file.read()
        print(t)

    # файл вне менеджера контекста
    print("---------------------")
    with open(filename) as file:
        content = file.readlines()
    for line in content:
        print(line.rstrip())

    # файл построчно
    print("---------------------")
    with open(filename) as file:
        for line in file:
            print(line.rstrip())


    # замена слова - better на ------
    print("---- replace better -----")
    with open(filename) as file:
        for line in file:
            rep_line = line.replace('better', '-------')
            print(rep_line.rstrip())

    print("\n------- guest book ---------")
    while True:
        name = input("Input your name (q to exit): ")
        if name == 'q':
            print("Goodbye!")
            break
        else:
            with open('guest_book', 'a') as file:
                file.write(name)
                file.write('\n')
            print("Nice to meet you, {}!".format(name.title()))

    print("\n ------ ex. 10-6 ---------")


    while True:
        try:
            add_1 = int(input('Input fisrt number: '))
            add_2 = int(input('Input second number: '))
        except ValueError:
            print("Your input is not digits! Try again ")
        else:
            res = add_1 + add_2
            print(res)
            break

    print("\n ------ ex. 10-8 ---------")
    try:
        with open('dogs.txt', 'r') as dogs:
            doggo = dogs.read()
            print(doggo)
    except FileNotFoundError:
        print("File dogs.txt is not found!")

    print("\n")
    try:
        with open('cats.txt', 'r') as cats:
            cato = cats.read()
            print(cato)
    except FileNotFoundError:
        print("File cats.txt is not found!")

    print("\n ------ ex. 10-11 ---------")
    try:
        with open('number.json') as file:
            number = json.load(file)

    except FileNotFoundError:
        number = input("Input your favorite number (I will remember it): ")
        with open('number.json', 'w') as file:
            json.dump(number, file)
    else:
        print("I know your favorite number! It is {}!".format(number))


    print("\n ------ ex. 10-13 ---------")
    greet_user()


