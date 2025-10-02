

class reposity:
    __data = {}

    @property
    def data(self):
        return self.__data

    # ключ для едениц измерения
    @staticmethod
    def measurement_key():
        return 'measurement model'

