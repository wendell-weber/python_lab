# TODO Написать 3 класса с документацией и аннотацией типов

import doctest
# Абстрактный класс йога
class Yoga:
    def __init__(self, style: str, duration: int):
        self.style = style  # Стиль йоги
        self.duration = duration  # Продолжительность занятия

    def start(self):
        # Запустить занятие
        ...

    def pause(self):
        # Поставить занятие на паузу
        ...

    def stop(self):
        # Закончить занятие
        ...
if __name__ == "__main__":
    doctest.testmod()