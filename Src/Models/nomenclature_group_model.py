from Src.Core.validator import validator
from Src.Core.abstract_model import abstact_model

###############################################
# Модель группы номенклатуры
# Категория для группировки товаров/материалов
# Содержит название и подробное описание категории
###############################################
class nomenclature_group_model(abstact_model):
    # Текстоваое описание группы номенклатуры
    __description: str = ""

    def __init__(self, name: str =None, description: str = None):
        super().__init__()
        if name is not None: self.name = name
        if description is not None: self.description = description

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

