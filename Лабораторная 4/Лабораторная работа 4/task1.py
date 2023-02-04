class Car:
    """Базовый класс автомобиля"""
    def __init__(self, model: str, weight: int, color: str):
        self._model = model #атрибут непубличный, так как модель автомобиля нельзя менять
        self._weight = weight #атрибут непубличный, так как массу автомобиля нельзя менять
        self.color = color

    def __str__(self) -> str:
        return f'Автомобиль "{self._model}": масса {self._weight}, цвет {self.color}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._model!r}, {self._weight!r}, {self.color!r})'

    def car_painting(self, color) -> str:
        """Смена цвета автомобиля"""
        ...

    def __eq__(self, other):
        """Сравниваем два автомобиля"""
        ...


class Passenger_Car(Car):
    """Дочерний класс легкового автомобиля"""
    def __init__(self, model: str, weight: int, color: str, body_type: str):
        super().__init__(model, weight, color)
        self._body_type = body_type #атрибут непубличный, так как тип кузова автомобиля нельзя менять

    def __str__(self) -> str:
        return f'Легковой автомобиль "{self._model}": масса {self._weight}, цвет {self.color}, тип кузова {self._body_type}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._model!r}, {self._weight!r}, {self.color!r}, {self._body_type!r})'

    def __eq__(self, other) -> bool:
        """Сравниваем два автомобиля
           Метод перегружаем потому что теперь для сравнения двух автомобилей
           необходим тип кузова, которого не было в базовом классе"""
        ...


if __name__ == "__main__":
    car1 = Car(model = "SUZUKI", weight = 7000, color = "black")
    print(car1.__str__())
    print(car1.__repr__())
    car2 = Passenger_Car(model = "BMV", weight = 5000, color = "red", body_type = "SUV")
    print(car2.__str__())
    print(car2.__repr__())
