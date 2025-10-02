import unittest

from Src.reposity import reposity
from Src.start_service import start_service


# класс для проверки запуска (переиспользование )
class test_start(unittest.TestCase):
    __start_service: start_service = start_service()

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.__start_service.start()

    def test_start_service_rangeNotEmpty(self):
        # Подготовка

        # Действе

        # Проверка
        assert self.__len(start_service.data[ reposity.measurement_key()]) > 0
