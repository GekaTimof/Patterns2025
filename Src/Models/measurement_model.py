from Src.Core.validator import validator
from Src.Core.abstract_model import abstact_model

###############################################
# Модель единицы измерения для товаров/материалов
# Хранит коэффициент преобразования и базовую единицу
# Поддерживает конвертацию между разными единицами измерения
###############################################
class measurement_model(abstact_model):
    # Базовые еденицы измерения
    __base_unit: 'measurement_model'
    # Коэффициент соотношения текущей еденицы измерения к базовым еденицам измерения
    __coefficient: (float, int)
    # Словарь для хранения существующих экземпляров
    __instances: dict = {}

    def __init__(self, name: str, base_unit: 'measurement_model' = None, coefficient: (float, int) = 1):
        # Если экземпляр с таким именем уже существует, возвращаем его
        if name in measurement_model.__instances:
            exist_instance = measurement_model.__instances[name]
            self.__dict__ = exist_instance.__dict__
            return

        super().__init__()
        self.name = name
        self.coefficient = coefficient
        self.base_unit = base_unit if base_unit is not None else self

        # Сохраняем новый экземпляр
        measurement_model.__instances[name] = self

    @property
    def coefficient(self) -> (float, int):
        return self.__coefficient

    @coefficient.setter
    def coefficient(self, value: (float, int)):
        validator.validate(value, (float, int), min_lim_=0)
        self.__coefficient = value

    @property
    def base_unit(self) -> 'measurement_model':
        return self.__base_unit

    @base_unit.setter
    def base_unit(self, value: 'measurement_model'):
        validator.validate(value, measurement_model)
        self.__base_unit = value


    # универсальный метод (фабричный), для создания едениц измерения
    @staticmethod
    def create(name: str, base_unit: 'measurement_model' = None, coefficient: (float, int) = 1) -> 'measurement_model':
        validator.validate(name, str)
        item = measurement_model(name)
        if base_unit is not None:
            validator.validate(base_unit, measurement_model)
            item.base_unit = base_unit
        validator.validate(coefficient, (float, int), min_lim_=0)
        item.coefficient = coefficient

        return item


    # метод для создания граммов
    @staticmethod
    def create_gram() -> 'measurement_model':
        return measurement_model.create("gram")

    # метод для создания килограмма
    @staticmethod
    def create_kilogram():
        base_unit = measurement_model.create_gram()
        return measurement_model.create("kilogram", base_unit, 1000)

    # метод для создания граммов
    @staticmethod
    def create_liter() -> 'measurement_model':
        return measurement_model.create("liter")

    # метод для создания килограмма
    @staticmethod
    def create_milliliter():
        base_unit = measurement_model.create_liter()
        return measurement_model.create("milliliter", base_unit, 0.001)