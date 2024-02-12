class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self.pages = value
        else:
            raise ValueError("Pages must be a positive integer")

    def __repr__(self):
        return f"PaperBook('{self.name}', '{self.author}', {self.pages})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, float) and value > 0:
            self.duration = value
        else:
            raise ValueError("Duration must be a positive float")

    def __repr__(self):
        return f"AudioBook('{self.name}', '{self.author}', {self.duration})"
