
pas = input("Введите пароль: ")
if len(pas) < 5:
    print("Слишком короткий пароль!")
elif pas[0:6] == "qwerty":
    print("Ненадёжный пароль!")
else:
    print("Ок.")

def p1():
    n = int(input('Введите номер вашего места в плацкартном вагоне: '))
    print()
    if n > 36:
        print('Ваше место - боковое.')
    elif n % 2:
        print('Ваше место в купе внизу.')
    else:
        print('Ваше место в купе наверху.')

def p2():
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Да, весокосный")
    else:
        print("Нет, не весокосный")

def p3():
    a = input()
    b = input()
    if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
        print('фиолетовый')
    elif a == 'красный' and b == 'красный':
        print('красный')
    elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
        print('оранжевый')
    elif a == 'желтый' and b == 'желтый':
        print('желтый')
    elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
        print('зеленый')
    elif a == 'синий' and b == 'синий':
        print('синий')
    else:
        print('ошибка цвета')


p1()
p2()
p3()

