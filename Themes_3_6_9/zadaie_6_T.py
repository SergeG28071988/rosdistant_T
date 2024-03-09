# Напишите программу, которая создает список, заполняет его случайными элементами, и сохраняет этот список в текстовом файле.

import random

def create_random_list(size):
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(1, 100))
    return random_list

def save_list_to_file(random_list, filename):
    try:
        with open(filename, 'w') as file:
            for num in random_list:
                file.write(str(num) + '\n')
        print("Список успешно сохранен в файле", filename)
    except IOError:
        print("Ошибка при сохранении списка в файле", filename)

def main():
    try:
        size = int(input("Введите размер списка: "))
        filename = input("Введите имя файла для сохранения списка: ")

        random_list = create_random_list(size)
        save_list_to_file(random_list, filename)
    except ValueError:
        print("Ошибка! Введите целое число для размера списка.")

main()
