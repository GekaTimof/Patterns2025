from Src.Core.validator import validator
from Src.Core.abstract_model import abstact_model

###############################################
# Модель группы номенклатуры
class nomenclature_group_model(abstact_model):
    __description: str = ""

    """
    Полное описание группы 
    """
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        validator.validate(value, str)
        self.__description = value.strip()

