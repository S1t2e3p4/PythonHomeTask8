def check_input_1():
    number = input()
    while not int(number) in (1, 2, 3, 4, 5, 6, 7):
        print('Введено некорректное значение. Повторите ввод данных')
        number = input()
    return number


def check_input_2():
    number = input()
    while not int(number) in (1, 2):
        print('Введено некорректное значение. Повторите ввод данных')
        number = input()
    return number