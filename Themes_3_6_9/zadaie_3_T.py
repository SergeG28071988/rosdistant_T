# Напишите программу, которая запрашивает у пользователя два числа, затем предлагает пользователю выбрать операцию (сложение, вычитание, умножение или деление) и выводит результат выбранной операции

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ZeroDivisionError("Ошибка! Деление на ноль.")

def calculate():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")

        choice = int(input("Введите номер операции: "))

        result = 0

        if choice == 1:
            result = add(num1, num2)
            print("Результат сложения:", result)
        elif choice == 2:
            result = subtract(num1, num2)
            print("Результат вычитания:", result)
        elif choice == 3:
            result = multiply(num1, num2)
            print("Результат умножения:", result)
        elif choice == 4:
            result = divide(num1, num2)
            print("Результат деления:", result)
        else:
            print("Ошибка! Неверный номер операции.")
    except ValueError:
        print("Ошибка! Введите числа.")
    except ZeroDivisionError as e:
        print(e)

calculate()
