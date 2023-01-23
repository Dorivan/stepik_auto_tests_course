import math
import os


def calc(x): return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(current_dir)
    print(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
