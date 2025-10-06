import unittest
from Src.reposity import reposity
from Src.start_service import start_service


# Пласс для проверки запуска (переиспользование )
class test_start(unittest.TestCase):
    __start_service: start_service = start_service()

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.__start_service.start()


    # Проверка, что при старте сервиса создаются начальные еденицы измерения
    def test_start_service_rangeNotEmpty(self):
        # Подготовка

        # Действе

        # Проверка
        assert len(self.__start_service.data()) > 0


    # Проверка, что единицы измерения с одинаковым названием это одни и те же еденица измерения
    def test_measurement_relationships(self):
        # Подготовка
        kilogram = self.__start_service.data()[reposity.measurement_key]['kg']
        gram = self.__start_service.data()[reposity.measurement_key]['gr']

        # Действе

        # Проверка
        assert kilogram.base_unit == gram


    # Проверка создания единиц измерения
    def test_measurements_created(self):
        # Подготовка
        measurements = self.__start_service.data()[reposity.measurement_key]

        # Действие

        # Проверка
        assert 'gr' in measurements
        assert 'kg' in measurements
        assert measurements['gr'].name == "gram"
        assert measurements['kg'].name == "kilogram"


    # Проверка установки коэффициента преобразования
    def test_measurement_coefficient(self):
        # Подготовка
        kilogram = self.__start_service.data()[reposity.measurement_key]['kg']

        # Действие

        # Проверка
        assert kilogram.coefficient == 1000


    # Проверка Singleton паттерна
    def test_singleton_pattern(self):
        # Подготовка
        service1 = start_service()
        service2 = start_service()

        # Действие

        # Проверка
        assert service1 is service2


    # Проверка создания групп номенклатур
    def test_nomenclature_groups_creation(self):
        # Подготовка
        groups = self.__start_service.data()[reposity.nomenclature_group_key]

        # Действие

        # Проверка
        assert 'ММП' in groups
        assert groups['ММП'].name == 'ММП'
        assert groups['ММП'].description == 'Мясо и мясные продукты'


    # Проверка создания номенклатур
    def test_nomenclature_creation(self):
        # Подготовка
        nomenclatures = self.__start_service.data()[reposity.nomenclature_key]
        measurement = self.__start_service.data()[reposity.measurement_key]['kg']

        # Действие

        # Проверка
        assert 'Говядина' in nomenclatures
        assert nomenclatures['Говядина'].full_name == 'Говядина'
        assert nomenclatures['Говядина'].measurement == measurement