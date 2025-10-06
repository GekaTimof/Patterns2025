from Src.Core.validator import validator
from Src.Core.abstract_model import abstact_model
from Src.Models.measurement_model import measurement_model

###############################################
# Модель для хранения ингридиентов
# Хранит информацию о ингридиенте
# (название, количество, еденицы измерения)
###############################################
class ingredient_model(abstact_model):
    # Базовые еденицы измерения
    __base_unit: measurement_model
    # Количество (в базовых еденицах измерения)
    __amount: float

    def __init__(self, name: str = None,
                 base_unit: measurement_model = None, amount: float = None):
        super().__init__()
        if name is not None: self.name = name
        if base_unit is not None: self.base_unit = base_unit
        if amount is not None: self.amount = amount

    @property
    def __base_unit(self) -> measurement_model:
        return self.__base_unit

    @__base_unit.setter
    def __base_unit(self, value: measurement_model):
        validator.validate(value, measurement_model)
        self.__base_unit = value

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: str):
        validator.validate(value, float, min_lim_=0)
        self.amount = value