from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для '
           'вычисления квадратного корня из заданного числа')


def calculatesquareroot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(number):
    """Проверка числа."""
    if number <= 0:
        return
    i = calculatesquareroot(number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {i}')


print(message)
calc(25.5)
