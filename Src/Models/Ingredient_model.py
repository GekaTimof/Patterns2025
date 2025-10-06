from Src.Core.validator import validator
from Src.Core.abstract_model import abstact_model
from Src.Models.nomenclature_model import nomenclature_model

###############################################
# Модель для хранения ингридиентов
# Хранит информацию о ингридиенте
# (номенклатура, количество)
###############################################
class ingredient_model(abstact_model):
    # Номенклатура ингредиента
    __nomenclature: nomenclature_model
    # Количество (в базовых еденицах измерения)
    __amount: float

    def __init__(self, nomenclature: nomenclature_model = None, amount: (float, int) = None):
        super().__init__()
        if nomenclature is not None: self.nomenclature = nomenclature
        # if base_unit is not None: self.base_unit = base_unit
        if amount is not None: self.amount = amount

    @property
    def nomenclature(self) -> nomenclature_model:
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        validator.validate(value, nomenclature_model)
        self.__nomenclature = value

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: (float, int)):
        validator.validate(value, (float, int), min_lim_=0)
        self.__amount = float(value)