# TODO Написать 3 класса с документацией и аннотацией типов

import doctest
# Класс торт
class Cake:
    def __init__(self, flavor: str, size: str):
        self.flavor = flavor  # Вкус торта
        self.size = size  # Размер торта

    def bake(self):
        # Запустить процесс выпечки
        ...

    def decorate(self):
        # Украсить торт
        ...

    def cut(self):
        # Нарезать торт на порции
        ...
if __name__ == "__main__":
    doctest.testmod()