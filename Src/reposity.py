
######################################
# Класс для хранения данных
# Хранит эталоннные данны и рецепты в data по ключам
# Ключи получаются через специальные методы
###############################################
class reposity:
    __data = {}

    @property
    def data(self):
        return self.__data

    # ключ для едениц измерения
    @staticmethod
    def measurement_key():
        return 'measurement model'

    # ключ для групп номенклатур
    @staticmethod
    def nomenclature_group_key():
        return 'nomenclature group'

    # ключ для номенклатур
    @staticmethod
    def nomenclature_key():
        return 'nomenclature'

    # ключ для рецептов
    @staticmethod
    def recipes_key():
        return 'recipes'
