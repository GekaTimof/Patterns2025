from abc import ABC
import uuid
from Src.Core.validator import validator

###############################################
# Абстрактная базовая модель для всех сущностей
# Содержит общие поля: ID, наименование
# Реализует базовую валидацию и сравнение объектов
###############################################
class abstact_model(ABC):
    # Уникальный идентификатор
    __unique_code:str
    # Имя объекта
    __name: str = ""

    def __init__(self) -> None:
        super().__init__()
        self.__unique_code = uuid.uuid4().hex

    """
    Уникальный код
    """
    @property
    def unique_code(self) -> str:
        return self.__unique_code
    
    @unique_code.setter
    def unique_code(self, value: str):
        validator.validate(value, str)
        self.__unique_code = value.strip()
    
    """
    Обычное наименование. Ограничение на поле - не длинее 50 символов
    """
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        validator.validate(value, str, 50)
        self.__name = value.strip()


    """
    Перегрузка штатного варианта сравнения
    """
    def __eq__(self, value: str) -> bool:
        return self.__unique_code == value
