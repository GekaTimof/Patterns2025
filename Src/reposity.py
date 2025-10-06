

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