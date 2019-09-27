import os
import shutil


def make_dir(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('{} - уже существует'.format(name))


def remove_dir(name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print('{} - папки не существует'.format(name))


def list_dir():
    lst = os.listdir()
    print(lst)


if __name__ == '__main__':
    print('--Задачи (easy)--')

    import os
    import shutil

    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.

    for i in range(1, 10):
        os.mkdir("dir_" + str(i))

    for i in range(1, 10):
        os.rmdir("dir_" + str(i))

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

    print([i for i in os.listdir() if os.path.isdir(i)])

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    name_file = os.path.realpath(__file__)
    shutil.copy(name_file, name_file + '.copy')
