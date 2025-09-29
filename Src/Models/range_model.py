from Src.Core.validator import validator
from Src.Core.abstract_model import abstact_model

class range_model(abstact_model):
    __coefficient: float
    __base_unit: 'range_model'

    def __init__(self, name: str, coefficient: float = 1, base_unit: 'range_model' = None):
        super().__init__()
        self.name = name
        self.coefficient = coefficient
        self.base_unit = base_unit if base_unit is not None else self

    @property
    def coefficient(self) -> float:
        return self.__coefficient

    @coefficient.setter
    def coefficient(self, value: float):
        validator.validate(value, float, min_lim_=0)
        self.__coefficient = value

    @property
    def base_unit(self) -> 'range_model':
        return self.__base_unit

    @base_unit.setter
    def base_unit(self, value: 'range_model'):
        validator.validate(value, range_model)
        self.__base_unit = value

