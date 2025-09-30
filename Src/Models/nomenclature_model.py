from Src.Core.validator import validator
from Src.Core.abstract_model import abstact_model
from Src.Models.nomenclature_group_model import nomenclature_group_model
from Src.Models.measurement_model import measurement_model

###############################################
# Модель номенклатуры
class nomenclature_model(abstact_model):
    __full_name: str = ""
    __nomenclature_group: nomenclature_group_model
    __measurement: measurement_model

    """
    Полное наименование. Ограничение на поле - не длинее 255 символов
    """
    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        validator.validate(value, str, 255)
        self.__full_name = value

    """
    Группа номенклатуры
    """
    @property
    def nomenclature_group(self) -> nomenclature_group_model:
        return self.__nomenclature_group

    @nomenclature_group.setter
    def nomenclature_group(self, value: nomenclature_group_model):
        validator.validate(value, nomenclature_group_model)
        self.nomenclature_group = value

    """
    Еденицы измерения
    """
    @property
    def measurement(self) -> measurement_model:
        return self.__measurement

    @measurement.setter
    def measurement(self, value: measurement_model):
        validator.validate(value, measurement_model)
        self.__measurement = value
