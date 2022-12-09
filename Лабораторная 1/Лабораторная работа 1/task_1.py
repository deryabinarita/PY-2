import doctest


class Laptop:
    def __init__(self, brend: str, color: str, screen_diameter: int):
        """
        Создание и подготовка к работе объекта "Ноутбук"
        
        :param brend: Фирма ноутбука
        :param color: Цвет ноутбука
        :param screen_diameter: Диаметр экрана ноутбука в сантиметрах
        
        Примеры:
        >>> laptop = Laptop(brend='ASUS', color='Red', screen_diameter=40)
        """
        if not isinstance(brend, str):
            raise TypeError("Фирма ноутбука должна быть типа str")
        self.brend = brend

        if not isinstance(color, str):
            raise TypeError("Цвет ноутбука должен быть типа str")
        self.color = color

        if not isinstance(screen_diameter, int):
            raise TypeError("Диаметр экрана ноутбука должен быть типа int")
        if screen_diameter < 0:
            raise ValueError("Диаметр экрана должен быть положительным числом")
        self.screen_diameter = screen_diameter

    def is_the_laptop_asus(self) -> bool:
        """
        Функция, которая проверяет является ли ноутбук фирмы ASUS

        :return: Является ли ноутбук фирмы ASUS

        Примеры:
        >>> laptop = Laptop(brend='ASUS', color='Red', screen_diameter=40)
        >>> laptop.is_the_laptop_asus()
        """
        ...

    def change_color(self, new_color: str) -> None:
        """
        Функция, которая меняет цвет ноутбука
        :param new_color: Новый цвет ноутбука
        :raise TypeError: Если новый цвет ноутбука не типа str
        :return: Ничего
        """
        ...


class RubiksCube:
    def __init__(self, size: int, shape: str):
        """
        Создание и подготовка к работе объекта "Кубик Рубика"
        :param size: Размеры кубика (сколько элементарных ячеек на одной стороне кубика)
        :param shape: Форма кубика

        Пример:
        >>> cube1 = RubiksCube (size = 6, shape = 'tetrahedron')
        """

        if not isinstance(size, int):
            raise TypeError("Размеры кубика должны быть типа int")
        self.size = size

        self.shape = shape

    def is_the_cube_standart(self, size, shape) -> bool:
        """
        Функция проверяет является ли кубик формой куба и размерами 9
        :param size: Размер
        :param shape: Форма
        :return: Zвляется ли кубик стандартным

        Пример:
        >>> cube2 = RubiksCube (size = 9, shape = 'cube')
        >>> cube2.is_the_cube_standart()
        """
        ...

    def solve_cube(self):
        """
        Функция, которая собирает кубик
        :return: Ничего
        """
        ...


class Cake:
    def __init__(self, color: str, weight: int, manufacturer: str):
        """
        Создание и подготовка к работе объекта "Пироженое"
        :param color: Цвет пироженого
        :param weight: Масса в граммах
        :param manufacturer: Производитель (название компании)

        Пример
        >>> cake1 = Cake(color = 'red', weight = 250, manufacturer = 'Metropol')
        """

        self.color = color

        if not isinstance(weight, int):
            raise TypeError("Вес пироженого должен быть типа str")
        if weight < 0:
            raise ValueError("Масса пироженого болжна быть больше нуля")
        self.weight = weight

        if not isinstance(manufacturer, str):
            raise TypeError("Производитель должен быть типа str")
        self.manufacturer = manufacturer

    def is_carat_plus_cake(self, manufacturer) -> bool:
        """
        Функция проверяет является ли данное пироженое фирмы Карат Плюс
        :return: Является ли данное пироженое фирмы Карат Плюс

        Пример:
        >>> cake2 = Cake(color = 'red', weight = 100, manufacturer = 'Metropol')
        >>> cake2.is_carat_plus_cake(manufacturer = 'Metropol')
        """
        ...

    def eat_cake(self):
        """
        Функция, выполняющая поедание пироженого
        :return: Ничего
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
