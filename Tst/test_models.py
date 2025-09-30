from Src.settings_manager import settings_manager
from Src.Models.company_model import company_model
import unittest
from Src.Models.storage_model import storage_model
from Src.Models.measurement_model import measurement_model
from Src.Models.nomenclature_group_model import nomenclature_group_model
from Src.Models.nomenclature_model import nomenclature_model
import uuid

############################################################################

class test_models(unittest.TestCase):
    # Провери создание основной модели
    # Данные после создания должны быть пустыми
    def test_empty_create_company_model(self):
        # Подготовка
        model = company_model()

        # Действие

        # Проверки
        assert model.name == ""
        assert model.inn == 0
        assert model.bic == 0
        assert model.corr_account == 0
        assert model.account == 0
        assert model.ownership == ""


    # Проверить создание основной модели
    # Данные меняем. Данные должны быть
    def test_notEmpty_create_company_model(self):
        # Подготовка
        model = company_model()
        
        # Действие
        model.name = "test"
        model.inn = 1234
        model.bic = 2345
        model.corr_account = 3456
        model.account = 4567
        model.ownership = "ООО"
        
        # Проверки
        assert model.name != ""
        assert model.inn == 1234
        assert model.bic == 2345
        assert model.corr_account == 3456
        assert model.account == 4567
        assert model.ownership == "ООО"


    # Проверить создание основной модели
    # Данные загружаем через json настройки
    def test_load_create_company_model(self):
        # Подготовка
       file_name = "settings.json"
       manager = settings_manager()
       manager.file_name = file_name
       
       # Действие
       result = manager.load()
            
       # Проверки
       print(manager.file_name)
       assert result == True


    # Проверить создание основной модели
    # Данные загружаем. Проверяем работу Singletone
    def test_loadCombo_create_company_model(self):
        # Подготовка
        file_name = "./settings.json"
        manager1 = settings_manager()
        manager1.file_name = file_name
        manager2 = settings_manager()
        check_inn = 123456789

        # Действие
        manager1.load()

        # Проверки
        assert manager1.settings == manager2.settings
        print(manager1.file_name)
        assert(manager1.settings.company.inn == check_inn )
        print(f"ИНН {manager1.settings.company.inn}")


    # Проверка на сравнение двух по значению одинаковых моделей
    def text_equals_storage_model_create(self):
        # Подготовка
        id = uuid.uuid4().hex
        storage1 = storage_model()
        storage1.id = id
        storage2 = storage_model()   
        storage2.id = id
        # Действие GUID

        # Проверки
        assert storage1 == storage2


############################################################################

    # Проверка создания модели валюты
    # Создаём пустую модель, данных должно не быть
    def test_empty_create_measurement_model(self):
        # Подготовка
        measurement = measurement_model("г")

        # Действие GUID

        # Проверки
        assert measurement.coefficient == 1


    # Проверка создания модели валюты
    # Заполненные данные, данные должны быть
    def test_notEmpty_create_measurement_model(self):
        # Подготовка
        base_measurement = measurement_model("г")
        additional_measurement = measurement_model("кг", 1000, base_measurement)

        # Действие GUID

        # Проверки
        assert additional_measurement.base_unit == base_measurement


############################################################################

    # Проверка создания модели группы номенклатуры
    # Создаём пустую модель, модель должна быть созданна, но без данных
    def test_empty_create_nomenclature_group_model(self):
        # Подготовка
        nomenclature_group = nomenclature_group_model()

        # Действие GUID

        # Проверки
        assert nomenclature_group != None
        assert nomenclature_group.description == ""

    # Проверка создания модели группы номенклатуры
    # Заполненные данные, данные должны быть
    def test_notEmpty_create_nomenclature_group_model(self):
        # Подготовка
        nomenclature_group = nomenclature_group_model()

        # Действие GUID
        nomenclature_group.description = "test"

        # Проверки
        assert nomenclature_group.description == "test"


############################################################################

    # Проверка создания модели валюты
    # Создаём пустую модель, модель должна быть созданна, но без данных
    def test_empty_create_nomenclature_model(self):
        # Подготовка
        nomenclature =  nomenclature_model()

        # Действие GUID

        # Проверки
        assert nomenclature != None
        assert nomenclature.full_name == ""


    # Проверка создания модели валюты
    # Заполненные данные (единицы измерения), данные должны быть
    def test_NotEmpty_create_nomenclature_model(self):
        # Подготовка
        nomenclature = nomenclature_model()
        measurement = measurement_model("g")

        # Действие GUID
        nomenclature.measurement = measurement

        # Проверки
        assert nomenclature.measurement == measurement


if __name__ == '__main__':
    unittest.main()   
