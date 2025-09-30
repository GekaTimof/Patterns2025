from Src.Core.validator import validator
from Src.Core.abstract_model import abstact_model

class measurement_model(abstact_model):
    __coefficient: (float, int)
    __base_unit: 'measurement_model'

    def __init__(self, name: str, coefficient: (float, int) = 1, base_unit: 'measurement_model' = None):
        super().__init__()
        self.name = name
        self.coefficient = coefficient
        self.base_unit = base_unit if base_unit is not None else self

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

