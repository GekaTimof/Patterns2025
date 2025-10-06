from Src.Models.measurement_model import measurement_model
from Src.reposity import reposity

class start_service:
    __repo: reposity = reposity()

    def __init__(self):
        self.__repo.data[reposity.measurement_key] = []

    # Singletone
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(start_service, cls).__new__(cls)
        return cls.instance

    def __default_create_measurements(self):
        self.__repo.data[reposity.measurement_key].append(measurement_model.create_gram())
        self.__repo.data[reposity.measurement_key].append(measurement_model.create_kilogram())

    # Стартовый набор данных
    def data(self):
        return self.__repo.data

    # Основной метод для генерации эталонных данных
    def start(self):
        self.__default_create_measurements()


