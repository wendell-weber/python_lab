if __name__ == "__main__":
    # Write your solution here
    pass
class Rocket:
    """ Базовый класс ракеты """

    def __init__(self, name: str, engine_type: str):
        """ name (str): Название ракеты. engine_type (str): Тип двигателя."""
        self.name = name
        self.engine_type = engine_type

    def __str__(self):
        return f"{self.name} Rocket"

    def __repr__(self):
        return f"{self.name} Rocket"


class BallisticRocket(Rocket):
    """ Дочерний класс баллистические ракеты """

    def __init__(self, name: str, engine_type: str, warhead_type: str):
        """ name (str): Название ракеты. engine_type (str): Тип двигателя. warhead_type (str): Тип боеголовки """
        super().__init__(name, engine_type)
        self.warhead_type = warhead_type

    def __str__(self):
        return f"{self.name} Ballistic Rocket"

    def __repr__(self):
        return f"{self.name} Ballistic Rocket"

    def launch(self):
        return f"{self.name} Ballistic Rocket launched!"


class GuidedRocket(Rocket):


    def __init__(self, name: str, engine_type: str, guidance_system: str):
        """ name (str): Название ракеты. engine_type (str): Тип двигателя. guidance_system (str): Тип системы наведения """
        super().__init__(name, engine_type)
        self.guidance_system = guidance_system

    def __str__(self):
        return f"{self.name} Guided Rocket"

    def __repr__(self):
        return f"{self.name} Guided Rocket"

    def launch(self):
        return f"{self.name} Guided Rocket launched!"

    def assist_guidance_system(self):
        return f"{self.name} Guided Rocket guidance system assisted!"