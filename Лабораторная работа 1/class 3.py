# TODO Написать 3 класса с документацией и аннотацией типов

import doctest
# Класс цветок
class Flower:
    def __init__(self, type: str, color: str):
        self.type = type  # Тип цветка
        self.color = color  # Цвет цветка

    def water(self):
        # Полить цветок
        ...

    def fertilize(self):
        # Удобрить цветок
        ...

    def prune(self):
        # Подрезать цветок
        ...

if __name__ == "__main__":
    doctest.testmod()