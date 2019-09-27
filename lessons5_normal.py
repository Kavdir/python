import os
import lessons5_easy


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def change_dir(path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return ('dir_{} - папки не существует'.format(path))


answer = ''
while answer != '0':
    print('[1] - Перейти в папку')
    print('[2] - Просмотреть содержимое текущей папки')
    print('[3] - Удалить папку')
    print('[4] - Создать папку')
    print('[0] - Выход')
    answer = input('Выбрать: ')
    print(answer)
    if answer == '1':
        dir_name = input('наберите полный путь папки: ')
        print(change_dir(dir_name))
    elif answer == '2':
        dir_name = os.getcwd()
        lessons5_easy.list_dir()
    elif answer == '3':
        dir_name = input('наберите полный путь папки: ')
        lessons5_easy.remove_dir(dir_name)
    elif answer == '4':
        dir_name = input('наберите полный путь папки: ')
        lessons5_easy.make_dir(dir_name)
    elif answer == '0':
        break
    else:
        print('Такого пункта меню нет')
