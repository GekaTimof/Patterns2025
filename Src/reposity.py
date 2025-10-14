import inspect
"""
Репозиторий данных
"""
class reposity:
    __data = {}

    @property
    def data(self):
        return self.__data
    
    """
    Ключ для единц измерений
    """
    @staticmethod
    def range_key():
        return "range_model"
    

    """
    Ключ для категорий
    """
    @staticmethod
    def group_key():
        return "group_model"
    

    """
    Ключ для номенклатуры
    """
    @staticmethod
    def nomenclature_key():
        return "nomenclature_model"
    

    """
    Ключ для рецептов
    """
    @staticmethod
    def receipt_key():
        return "receipt_model"
    

    """
    Инициализация
    """
    def initalize(self):
        # получаем список свех методов класс и оставляем только методы ключей (_key на конце)
        methods = [m[0] for m in inspect.getmembers(reposity, predicate=inspect.isfunction) if not m[0].startswith("__")]
        keys = [i for i in methods if "_key" in i ]

        for key in keys:
            self.__data[getattr(reposity,key)()] = []
        # self.__data[ reposity.range_key() ] = []
        # self.__data[ reposity.group_key() ] = []
        # self.__data[ reposity.nomenclature_key() ] = []
        # self.__data[ reposity.receipt_key() ] = []
    
    
